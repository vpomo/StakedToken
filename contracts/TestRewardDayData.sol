// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

contract TestRewardDayData  {

    uint256 public constant MIN_STAKED_TIME = 30 days;

	function getRewardDayData(uint256 currentTime, uint256 beginTime, uint256 finishTime, uint256 lastTime) public pure //for test public
	    returns (uint256 dayCount, uint256 startDay) {
		if (currentTime > beginTime + MIN_STAKED_TIME) {
			if (lastTime > 0) {
				if (lastTime >= finishTime) { //ok
					return (0, getDayNumber(lastTime));
				}
				if (finishTime == 0) {
   					if (currentTime > lastTime + MIN_STAKED_TIME) { //ok
						return ((currentTime - lastTime) / 1 days, getDayNumber(lastTime));
					} else { //ok
						return (0, getDayNumber(lastTime));
					}
				} else {
					if (currentTime > finishTime + MIN_STAKED_TIME) { //ok 11
						return ((finishTime - lastTime) / 1 days, getDayNumber(lastTime));
					} else { //ok 10
						return ((currentTime - (lastTime + MIN_STAKED_TIME)) / 1 days, getDayNumber(lastTime));
					}
				}
			} else {
				if (finishTime == 0) { //ok
					uint256 rewardDayCount = (currentTime - (beginTime + MIN_STAKED_TIME)) / 1 days;
					return (rewardDayCount, getDayNumber(beginTime));
				} else {
					if (currentTime > finishTime + MIN_STAKED_TIME) { //ok
						return ((finishTime - beginTime) / 1 days, getDayNumber(beginTime));
					} else { //ok
						return ((currentTime - (beginTime + MIN_STAKED_TIME)) / 1 days, getDayNumber(beginTime));
					}
				}
			}
		}
		return (0, getDayNumber(beginTime));
	}

    function getDayNumber(uint256 timestamp) public pure returns (uint256) {
		return timestamp / 1 days;
	}

}

/*
// https://www.unixtimestamp.com/
DAY_IN_SECONDS = 86400

beginTime = 1642881900 (19014)
finishTime = 
lastTime = 
currentTime =  
=====================================
1. finishTime = 0
lastTime = 0 
currentTime = 20 days = 1644609900
(0, 19014)
=====================================
2. finishTime = 0
lastTime = 0 
currentTime = 32 days = 1645646700
(2, 19014)
=====================================
3. finishTime = 2 days = 1643054700
lastTime = 0 
currentTime = 32 days = 1645646700
(2, 19014)
=====================================
4. finishTime = 4 days = 1643227500
lastTime = 0 
currentTime = 38 days = 1646165100
(4, 19014)
=====================================
=====================================
5. finishTime = 4 days = 1643227500
lastTime = 2 days =  1643054700
currentTime = 38 days = 1646165100
(2, 19016)
=====================================
5. finishTime = 4 days = 1643227500
lastTime = 5 days =  1643313900
currentTime = 38 days = 1646165100
(0, 19019)
=====================================
6. finishTime = 4 days = 1643227500
lastTime = 0 
currentTime = 20 days = 1644609900
(0, 19014)
=====================================
7. finishTime = 4 days = 1643227500
lastTime = 5 days =  1643313900 
currentTime = 20 days = 1644609900
(0, 19014)
=====================================
8. finishTime = 4 days = 1643227500
lastTime = 5 days =  1643313900 
currentTime = 38 days = 1646165100
(0, 19019)
=====================================
9. finishTime = 0
lastTime = 5 days =  1643313900 
currentTime = 20 days = 1644609900
(0, 19014)
=====================================
9. finishTime = 0
lastTime = 5 days =  1643313900 
currentTime = 38 days = 1646165100
(0, 19019)
=====================================
10. finishTime = 4 days = 1643227500
lastTime = 1 days =  1642968300 
currentTime = 32 days = 1645646700
(1, 19015)
=====================================
11. finishTime = 4 days = 1643227500
lastTime = 1 days =  1642968300 
currentTime = 38 days = 1646165100
(3, 19015)
=====================================

*/