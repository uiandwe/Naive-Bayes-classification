# Naive-Bayes-classification

조건부 확률로 만든 문장의 긍정/부정 구하기
===================



해당 문장이 긍정인지 부정인지를 **조건부 확률**로  판단하는 간단한 **파이선** 로직입니다.

----------


필수사항
-------------

해당 문장을 분석하기 위해 파이썬 한글 형태소 분석기인 **konlpy**를 사용하였습니다.

<i class="icon-file"></i> 설치 참조 : http://konlpy.org/

긍정 / 부정에 대한 자료는 /word/*.sql 파일에 있습니다.



> **Note:**

> - 긍정 / 부정에 대한 원본 데이터는 /word/*.txt 에 있습니다.
> - 해당 데이터를 영어 긍정 / 부정을 기본으로 네이버 사전을 크롤링하여 만들어 **오류가 있을수 있습니다.**


#### <i class="icon-file"></i> 필요 라이브러리

pymysql	:	https://pypi.python.org/pypi/PyMySQL
konlpy		:	http://konlpy.org/



조건부 확률 공식
--------------------

확률 공간 Ω에서의 두 사건 A, B에 대해서 P(B) > 0일 때 사건 B가 일어났을 때 사건 A의 조건부 확률은
![](https://github.com/uiandwe/Naive-Bayes-classification/blob/master/Bayes'%20theorem.png)

긍정 부정 두가지 상황이 있으므로


P(c) = 1/2

P1(x|c) = count(해당 문장에서 긍정 단어 리스트 수 ) / count(전체 긍정 단어 리스트 수 )

P2(x|c) = count(해당 문장에서 부정 단어 리스트 수 ) / count(전체 부정 단어 리스트 수 )

```
if p1 > p2:

  긍정

else:

  부정
```
