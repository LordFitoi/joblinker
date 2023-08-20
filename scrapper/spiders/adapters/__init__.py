from .himalayas import HimalayasAdapter
from .nodesk import NoDeskAdapter


ADAPTERS = {
    "https://himalayas.app/jobs": HimalayasAdapter(),
    "https://nodesk.co/remote-jobs": NoDeskAdapter(),
}
