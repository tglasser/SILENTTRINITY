import pytest
import requests
import sys
import os
import random
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

<<<<<<< HEAD
from core.teamserver.loader import Loader
from core.teamserver.listener import Listener
=======
from silenttrinity.core.teamserver.loader import Loader
from silenttrinity.core.teamserver.listener import Listener
from silenttrinity.core.utils import create_self_signed_cert

CERT_PATH = "./tests/cert.pem"
KEY_PATH = "./tests/key.pem"
CHAIN_PATH = "./tests/chain.pem"

for f in list(filter(lambda x: os.path.exists(x) == True, [CERT_PATH, KEY_PATH, CHAIN_PATH])):
    os.remove(f)
>>>>>>> 239e4fcf5f821b00057909109a59f24a9322359f

@pytest.fixture
def listener_loader():
    ''' Load all of the listeners'''
<<<<<<< HEAD
    return Loader(type="listener", paths=["core/teamserver/listeners/"])
=======
    return Loader(type="listener", paths=["silenttrinity/core/teamserver/listeners/"])

def test_self_signed_cert_creation():
    create_self_signed_cert(
        key_file = KEY_PATH,
        cert_file = CERT_PATH,
        chain_file = CHAIN_PATH
    )

    assert len(list(filter(lambda x: os.path.exists(x) == True, [CERT_PATH, KEY_PATH, CHAIN_PATH]))) == 3
>>>>>>> 239e4fcf5f821b00057909109a59f24a9322359f

def test_listeners(listener_loader):
    s = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=0.5
    )
    s.verify = False
    s.mount('http://', HTTPAdapter(max_retries=retries))
    s.mount('https://', HTTPAdapter(max_retries=retries))

    for l in listener_loader.loaded:
        print(f"Testing listener '{l.name}'")
        assert isinstance(l, Listener) == True

        if l.name in ['http', 'https']:
            l['BindIP'] = '127.0.0.1'
            l['Port'] = str(random.randint(3000, 6000))
<<<<<<< HEAD
=======
            if l.name == 'https':
                l['Cert'] = CERT_PATH
                l['key'] = KEY_PATH
>>>>>>> 239e4fcf5f821b00057909109a59f24a9322359f
            l.start()
            r = s.get(f"{l.name}://127.0.0.1:{l['Port']}/")
            assert r.status_code == 404
            l.stop()
            assert l.running == False
