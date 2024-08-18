"""This module provides a class """

import asyncio

from src.exceptions.exception import AccessionIdsError, EntrySubsetError
from src.utils.util_functions import (
    generate_description_data,
    get_response_interpro,
    uniprot_id_regex_match,
)


async def get_accession_des(
    uniprot_id: str,
    entry_type: str,
) -> dict[str, list[str]]:
    """Get the accession ids and descriptions from the interpro API."""
    # check the uniprot id is valid using regex
    uniprot_id_regex_match(uniprot_id)

    # get the response from the interpro API
    response = get_response_interpro(uniprot_id)

    # get the entry_type
    entry_subset = response.get("entry_subset", None)

    if entry_subset is None:
        error_message = f"{entry_subset}{uniprot_id}."
        raise EntrySubsetError(error_message)

    # store the accession ids
    accessions_ids = [
        entry.get("accession")
        for entry in entry_subset
        if entry.get("entry_type", None) == entry_type
        and entry.get("accession", None) is not None
    ]

    if accessions_ids == []:
        error_message = (
            f"No accession ids found from the interpro API for {uniprot_id}."
        )
        raise AccessionIdsError(error_message)

    # pass the accession ids to get the descriptions
    return await generate_description_data(accessions_ids)


def run_accession_description(
    uniprot_id: str, entry_type: str
) -> dict[str, list[str]]:  # noqa: ANN001
    """Run function interpro API."""
    return asyncio.run(get_accession_des(uniprot_id, entry_type))


if __name__ == "__main__":
    uniprot_id = "P51587"
    entry_type = "superfamily"
    print(run_accession_description(uniprot_id, entry_type))
