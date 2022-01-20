from brownie import Wei, reverts
import brownie
import time

def test_staked_token(chain, accounts, interface, instance, graph, graph_whale):
    print('='*20 + ' running ... ' + '='*20)
    decimal = 1e18
    one_day = 60*60*24
    minStakedTime = 30 * one_day

    timestamp = int(time.time())
    print('totalSupply', graph.totalSupply()/decimal)
    print('balance GRT of graph_whale', graph.balanceOf(graph_whale)/decimal)

    amount = 1000*decimal

    graph.transfer(instance, amount*1000, {'from': graph_whale})

    graph.approve(instance, amount*1000, {'from': graph_whale})
    tx = instance.stake(graph_whale, amount, {'from': graph_whale})
    #print('tx = ', tx.info())

    instance.incrementShiftTime(one_day*3)

    graph.approve(instance, amount*1000, {'from': graph_whale})
    tx = instance.stake(graph_whale, amount, {'from': graph_whale})

    print('getCountStake', instance.getCountStake(graph_whale))
    print('getChangeRewardCount', instance.getChangeRewardCount())
    print('viewChangeRewardByIndex 0', instance.viewChangeRewardByIndex(0))
    dayNumber = instance.getCurrentDayNumber()
    print('dayNumber', dayNumber)
    print('viewCountStakesByDay', instance.viewCountStakesByDay(dayNumber))
    tx = instance.unStake(accounts[0], {'from': graph_whale})

    instance.incrementShiftTime(minStakedTime + one_day*5)

    print('viewUserStake', instance.viewUserStake(graph_whale))

    print('getRewardTokenAmount 19010', instance.getRewardTokenAmount(19010))
    print('getRewardTokenAmount 19012', instance.getRewardTokenAmount(19012))
    print('getRewardTokenAmount 19013', instance.getRewardTokenAmount(19013))
    print('getRewardTokenAmount 19014', instance.getRewardTokenAmount(19014))

    print('getCurrentCountStakes 19010', instance.getCurrentCountStakes(19010))
    print('getCurrentCountStakes 19011', instance.getCurrentCountStakes(19011))
    print('getCurrentCountStakes 19013', instance.getCurrentCountStakes(19013))
    print('getCurrentCountStakes 19014', instance.getCurrentCountStakes(19014))
    print('getCurrentCountStakes 19015', instance.getCurrentCountStakes(19015))

    print('calcReward - 8 - 19012:', instance.calcReward(8, 19012, amount))

    print('getDailyAmount 19011', instance.getDailyAmount(19011, amount))

    print('getDailyAmount 19012', instance.getDailyAmount(19012, amount))
    print('getDailyAmount 19013', instance.getDailyAmount(19013, amount))
    print('getDailyAmount 19014', instance.getDailyAmount(19014, amount))

    print('viewCountStakesByDay', instance.viewCountStakesByDay(19014))

    print('calcRewardByIndex 0', instance.calcRewardByIndex(graph_whale, 0))
    print('calcRewardByIndex 1', instance.calcRewardByIndex(graph_whale, 1))

    tx = instance.unStakeAny(accounts[0], 1, {'from': graph_whale})
