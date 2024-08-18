import asyncio
import re
from collections import defaultdict
from typing import Any

import aiohttp
import requests

from exceptions.exception import RegexError


# helper function for the regex match for uniprot id
def uniprot_id_regex_match(uniprot_id: str) -> str:
    """Check the uniprot id is valid using regex.

    Args: uniprot_id (str): The uniprot id to be checked.

    Returns: str: The uniprot id if it is valid.
    """
    # check the uniprot id is valid using regex
    uniprot_regexp = (
        r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}"
    )
    if not re.match(uniprot_regexp, uniprot_id):
        error_message = f"Invalid UniProt ID: {uniprot_id}"
        raise RegexError(error_message)

    return uniprot_id


def get_response_interpro(
    uniprot_id: str,
) -> Any:  # noqa: ANN401
    """Get the respons.
    Args: uniprot_id (str)
    Returns: JSON: The response from the interpro API.
    """
    response = requests.get(
        f"https://protein/UniProt/{uniprot_id}",  # noqa: E231,  # noqa: E501
        timeout=5,
    )
    response.raise_for_status()

    return response.json()


async def get_description_data_using_accessions_ids(
    accessions_ids: list[str],
    session: aiohttp.ClientSession,
) -> list[aiohttp.client._RequestContextManager]:
    """Get the response .

    Args: accessions_ids (list[str]):
    Returns: list[aiohttp.client._RequestContextManager]: API.
    """
    # get the response from the interpro API using accessions ids
    return [
        session.get(
            f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{accession_id}",  # noqa: E501
            ssl=False,
            raise_for_status=True,
            timeout=5,
        )
        for accession_id in accessions_ids
    ]


# helper function
async def generate_description_data(
    accessions_ids: list[str],
) -> dict[str, list[str]]:
    """Generate description data from accession_ids.

    Args: accessions_ids (list[str]):.

    Returns: dict[str, list[str]]:.
    """
    # process the accessions ids
    async with aiohttp.ClientSession() as session:
        tasks = await get_description_data_using_accessions_ids(
            accessions_ids, session
        )  # noqa: E501
        responses = await asyncio.gather(*tasks)
        accessions_ids_with_descriptions = defaultdict(list)
        for accession_id, response in zip(
            accessions_ids, responses, strict=False
        ):  # noqa: ANN002
            json_response = await response.json()  # noqa: ANN002
            accessions_ids_with_descriptions[
                accession_id
            ] = json_response.get(  # noqa: ANN002
                "metadata",
                {},
            ).get(
                "go_terms", None
            )
        return accessions_ids_with_descriptions
