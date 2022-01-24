Для контракта январской версии 2022 года
Основные функции:
1 - stake(address onBehalfOf, uint256 amount) - сделать стейк на адрес кошелька onBehalfOf, количество токенов amount
2 - unStake(address onBehalfOf) - забрать все стейки с пересылкой токенов на адрес onBehalfOf
3 - getReward(address onBehalfOf) - получить проценты в токенах на кошелек onBehalfOf
4 - unStakeAny(address onBehalfOf, uint256 index) - забрать стейк с пересылкой токенов на адрес onBehalfOf, где index - номер стейка, начиная с нуля 
(т.е. если было несколько стейков с одного кошелька)
5 - viewUserStake(address user) - просмотр данных о всех стейках. Возвращаются массивы (время начала стейка, время последнего снятия реворда, сумма стейка, флаг об окончании стейка)
6 - viewUserStakeAny(address user, uint256 index) - просмотр данных о стейке с любым номером. Возвращаются такие же переменные, как и в 5 пункте
7 - getCountStake(address user) - количество сделанных стейков для юзера
8 - getChangeRewardCount() - счетчик изменений показателя по количеству токенов для ежедневного распределения
9 - viewChangeRewardByIndex(uint256 index) - выводит по индексу номер дня и количеству токенов для ежедневного распределения, которое было установлено
10 - viewCountStakesByDay(uint256 dayNumber) - выводит количество активных стейков и количество застейканных токенов за какой-либо день
11 - getCurrentTime() - выводит текущее время в Unix-формате
12 - getCurrentDayNumber() - выводит текущий номер дня
13 - getDayNumber(uint256 timestamp) - по Unix-формат времени выводит номер дня
14 - calcRewardByIndex(address user, uint256 index, uint256 shiftTime) - выводит величину возможного профита. Если shiftTime == 0, то на текущий день, 
либо можно задать смещение в секундах, чтобы узнать будущий профит


15 - addRewardFund(uint256 amount) - (только овнер) - пополнение баланса для выплаты ревордов
16 - setRewardTokenByDay(uint256 newValue) - (только овнер) - изменение значения по текущему количеству токенов для ежедневного распределения.
Количество токенов в день можно менять, только один раз в сутки


17 - rewardTokensByDay - Переменная, в которой отображается текущее количество токенов для ежедневного распределения
18 - totalStakedTokens - Переменная, в которой отображается текущая сумма всех застейканных юзерами токенов
19 - totalReceivedReward - Переменная, в которой отображается текущая сумма всех полученных юзерами ревордов
20 - totalAddedTokenForReward - Переменная, в которой отображается текущая сумма всех токенов, переведенных админом для ревордов
21 - totalStakesCount - Переменная, в которой отображается текущее количество активных стейкеров

22 - incrementShiftTime(uint256 incValue) - это для проверки работы контракта. Любой может увеличить прошедшее время в контракте.
В окончательном коде этой функции не должно быть.