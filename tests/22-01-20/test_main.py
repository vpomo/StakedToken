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

    dayNumber = instance.getCurrentDayNumber()
    startTime = instance.getCurrentTime()

    instance.incrementShiftTime(one_day*2)

    instance.setRewardTokenByDay(200, {'from':  accounts[2]})

    instance.incrementShiftTime(one_day)

    instance.setRewardTokenByDay(400, {'from':  accounts[2]})

    graph.approve(instance, amount*1000, {'from': graph_whale})
    tx = instance.stake(graph_whale, amount, {'from': graph_whale})

    print('getCountStake', instance.getCountStake(graph_whale))
    print('getChangeRewardCount', instance.getChangeRewardCount())
    print('viewChangeRewardByIndex 0', instance.viewChangeRewardByIndex(0))
    print('viewChangeRewardByIndex 1', instance.viewChangeRewardByIndex(1))
    print('getCurrentTime', startTime)
    print('dayNumber', dayNumber)
    print('viewCountStakesByDay', instance.viewCountStakesByDay(dayNumber))

    tx = instance.unStakeAny(accounts[0], 0, {'from': graph_whale})

    print('totalStakesCount', instance.totalStakesCount())
    print('totalStakedTokens', instance.totalStakedTokens())

    instance.incrementShiftTime(minStakedTime + one_day*5)


    #print('getRewardTokenAmount 19010', instance.getRewardTokenAmount(19010))
    #print('getRewardTokenAmount 19012', instance.getRewardTokenAmount(19012))
    #print('getRewardTokenAmount 19013', instance.getRewardTokenAmount(19013))
    #print('getRewardTokenAmount 19014', instance.getRewardTokenAmount(19014))

    #print('getCurrentCountStakes 19010', instance.getCurrentCountStakes(19010))
    #print('getCurrentCountStakes 19011', instance.getCurrentCountStakes(19011))
    #print('getCurrentCountStakes 19013', instance.getCurrentCountStakes(19013))
    #print('getCurrentCountStakes 19014', instance.getCurrentCountStakes(19014))
    #print('getCurrentCountStakes 19015', instance.getCurrentCountStakes(19015))

    #print('calcReward - 8 - 19012:', instance.calcReward(8, 19012, amount))

    #print('getDailyAmount 19011', instance.getDailyAmount(19011, amount))

    #print('getDailyAmount 19012', instance.getDailyAmount(19012, amount))
    #print('getDailyAmount 19013', instance.getDailyAmount(19013, amount))
    #print('getDailyAmount 19014', instance.getDailyAmount(19014, amount))

    print('viewCountStakesByDay', instance.viewCountStakesByDay(19021))

    stakeInfo = instance.viewUserStakeAny(graph_whale, 0)
    print('viewUserStakeAny ()', stakeInfo)
    #print('getRewardDayData ()', instance.getRewardDayData(startTime, stakeInfo[1], 0, 35*86400))
    #print('getRewardDayData ()', instance.getRewardDayData(1642959247, 1643218450, 0, 35*86400))

    #print('tx = ', tx.info())
    print('calcRewardByIndex 0', instance.calcRewardByIndex(graph_whale, 0, 0))
    print('calcRewardByIndex 1', instance.calcRewardByIndex(graph_whale, 1, 0))

    tx = instance.getReward(accounts[1], {'from': graph_whale})
    #print('tx = ', tx.info())
    stakeInfo = instance.viewUserStakeAny(graph_whale, 0)
    print('viewUserStakeAny (0)', stakeInfo)

    stakeInfo = instance.viewUserStakeAny(graph_whale, 1)
    print('viewUserStakeAny (1)', stakeInfo)

    instance.incrementShiftTime(one_day)

    print('getCurrentTime', instance.getCurrentTime())

    print('calcRewardByIndex 0', instance.calcRewardByIndex(graph_whale, 0, 0))
    print('calcRewardByIndex 1', instance.calcRewardByIndex(graph_whale, 1, 0))

    #print('getRewardDayData 0', instance.getRewardDayData(1643018821, 1643278026, 1643278021, 0))

    #print('getRewardDayData 0', instance.getRewardDayData(1643278024, 0, 1643710024, 0))


    instance.incrementShiftTime(one_day)
    print('calcRewardByIndex 0', instance.calcRewardByIndex(graph_whale, 0, 0))
    print('calcRewardByIndex 1', instance.calcRewardByIndex(graph_whale, 1, 0))

    tx = instance.getReward(accounts[1], {'from': graph_whale})
    #print('tx = ', tx.info())

    #print('calcReward - 3 - 19015:', instance.calcReward(3, 19015, amount))

    #print('getDailyAmount 19012', instance.getDailyAmount(19015, amount))
    #print('getDailyAmount 19013', instance.getDailyAmount(19016, amount))
    #print('getDailyAmount 19014', instance.getDailyAmount(19017, amount))

    #print('getRewardTokenAmount 19015', instance.getRewardTokenAmount(19015))
    #print('getRewardTokenAmount 19016', instance.getRewardTokenAmount(19016))
    #print('getRewardTokenAmount 19017', instance.getRewardTokenAmount(19017))
    #print('getRewardTokenAmount 19018', instance.getRewardTokenAmount(19018))
    #print('getRewardTokenAmount 19019', instance.getRewardTokenAmount(19019))
    #print('getRewardTokenAmount 19020', instance.getRewardTokenAmount(19020))

    tx = instance.unStake(accounts[0], {'from': graph_whale})

    instance.incrementShiftTime(one_day)
    print('calcRewardByIndex 1', instance.calcRewardByIndex(graph_whale, 1, 0))
    tx = instance.getReward(accounts[1], {'from': graph_whale})
    print('tx = ', tx.info())
