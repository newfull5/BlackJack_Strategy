# BlackJack_Strategy
The number of case to win in BlackJack [Python]

 * 블랙잭에서 발생하는 경우의 수를 나열하여 확률을 계산하는 것을 목표로합니다.
 * 바닐라 파이썬과 시각화를 위한 matplotlib을 사용하였습니다.
 * ~정말로 블랙잭 전략을 알아보고자 하신다면 다른 좋은 자료를 참고하시는 것을 권장합니다.~


## Summary

### 1. CommonSense
* [1. CommonSense](https://github.com/newfull5/BlackJack_Strategy/blob/master/1.%20CommonSense.ipynb)<br>

* 딜러의 업카드가 2~6일 경우 딜러는 버스트할 확률이 높습니다. 도전적인 플레이를 감행해도 좋습니다.<br>

* 플레이어는 카드의 총합이 14이상일때 스탠드하는 편이 가장 승률이 높습니다. <br><br>

### 2. DoINeedToSplit

* [2. DoINeedToSplit](https://github.com/newfull5/BlackJack_Strategy/blob/master/2.%20DoINeedToSplit.ipynb)<br>

* **에이스 페어는 무조건 스플릿**해야합니다. 소프트 핸드의 이점도 잃고, 12라는 애매한 숫자로 시작하게됩니다.<br>

* 8페어도 스플릿해야합니다. 그렇지 않으면 16이라는 가장 불리한 숫자로 게임을 시작해야합니다.<br>

* 10,10은 절대로 스플릿해서는 안됩니다. 높은 확률로 이길 수 있는 기회를 버리는 셈입니다.<br><br>


### 3. CaseByCase

* [3. CaseByCase](https://github.com/newfull5/BlackJack_Strategy/blob/master/3.%20CaseByCase.ipynb)<br>

* 첫 패의 합이 5 ~ 8일 경우는 승률이 낮은 편입니다. 딜러의 업카드가 흑우카드(2 ~ 6)가 아니라면 사실상 졌다고 봐야할 것입니다.<br>

* 13~17까지는 사실상 딜러가 버스트 될 확률(25%)과 별반 다르지 않습니다. 서랜더를 허용한다면 최대한 사용도록 합니다.<br>

* 9~11인경우 승률이 좋습니다. 물론 스탠드를 해서는 안되고, 딜러의 업카드가 흑우카드라면 더블다운을 하도록 합니다.
