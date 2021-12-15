from brownie import Wei, reverts
import brownie
import time

def test_staked_token(chain, accounts, interface, instance, graph, graph_whale):
    print('='*20 + ' running ... ' + '='*20)
    decimal = 1e18
    one_day = 60*60*24

    timestamp = int(time.time())
    print('getWeekday', instance.getWeekday(timestamp))
    print('totalSupply', graph.totalSupply()/decimal)
    print('balance GRT of graph_whale', graph.balanceOf(graph_whale)/decimal)

    amount = 1000*decimal

    graph.approve(instance, amount, {'from': graph_whale})
    tx = instance.stake(graph_whale, amount, {'from': graph_whale})
    #print('tx = ', tx.info())

    print('getCountStake', instance.getCountStake(graph_whale))
    print('viewUserStake', instance.viewUserStake(graph_whale))

    chain.sleep(one_day*2)
    chain.mine()
    print('calcRewardByIndex', instance.calcRewardByIndex(graph_whale, 0))
    chain.sleep(one_day*2)
    chain.mine()
    print('calcRewardByIndex', instance.calcRewardByIndex(graph_whale, 0))

    instance.getReward(accounts[0], {'from': graph_whale})
    print('balance GRT of accounts[0]', graph.balanceOf(accounts[0])/decimal)
    chain.sleep(one_day*2)
    chain.mine()
    print('calcRewardByIndex', instance.calcRewardByIndex(graph_whale, 0))

    chain.sleep(one_day*21)
    chain.mine()
    print('calcRewardByIndex', instance.calcRewardByIndex(graph_whale, 0))
    instance.getReward(accounts[0], {'from': graph_whale})
    print('balance GRT of accounts[0]', graph.balanceOf(accounts[0])/decimal) # 290_000_000


    graph.approve(instance, amount, {'from': graph_whale})
    tx = instance.stake(graph_whale, amount, {'from': graph_whale})

    print('getWeekday', instance.getWeekday(timestamp))
    print('getCountStake', instance.getCountStake(graph_whale))
    print('viewUserStakeAny 0', instance.viewUserStakeAny(graph_whale, 0))
    print('viewUserStakeAny 1', instance.viewUserStakeAny(graph_whale, 1))

    chain.sleep(one_day*21)
    chain.mine()
    print('calcRewardByIndex 0', instance.calcRewardByIndex(graph_whale, 0))
    print('calcRewardByIndex 1', instance.calcRewardByIndex(graph_whale, 1))

    print('balance GRT of accounts[0] before', graph.balanceOf(accounts[0])/decimal) # 290_000_000
    instance.getReward(accounts[0], {'from': graph_whale})
    print('balance GRT of accounts[0] after', graph.balanceOf(accounts[0])/decimal) # 290_000_000

    print('viewUserStakeAny 0', instance.viewUserStakeAny(graph_whale, 0))
    print('viewUserStakeAny 1', instance.viewUserStakeAny(graph_whale, 1))


    print('balance GRT of accounts[0] before', graph.balanceOf(accounts[0])/decimal) # 290_000_000
    chain.sleep(one_day*65)
    chain.mine()
    tx = instance.unStake(accounts[0], {'from': graph_whale})
    print('tx = ', tx.info())
    print('balance GRT of accounts[0] after', graph.balanceOf(accounts[0])/decimal) # 290_000_000
