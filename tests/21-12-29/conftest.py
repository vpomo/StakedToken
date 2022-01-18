import pytest
from brownie import config

@pytest.fixture(scope="module")
def instance(StakedToken, accounts):
    return StakedToken.deploy('0xc944e90c64b2c07662a292be6244bdf05cda44a7', {'from': accounts[0]})

@pytest.fixture
def graph(interface):
    yield interface.ERC20('0xc944e90c64b2c07662a292be6244bdf05cda44a7')

@pytest.fixture
def graph_whale(accounts):
    # binance8
    yield accounts.at('0xf977814e90da44bfa03b6295a0616a897441acec', force=True)

@pytest.fixture
def vpomo(accounts):
    yield accounts.at('0x5a8C89E24417ee83F1b5B07a1608F7C0eF12E6E2', force=True)
