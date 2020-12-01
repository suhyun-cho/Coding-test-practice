{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## greedy 알고리즘 문제 - 잃어버린 괄호\n",
    "2020-12-01\n",
    "\n",
    "#### 문제설명\n",
    "세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.\n",
    "<br>\n",
    "그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.<br>\n",
    "\n",
    "괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.<br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 작은값을 만들기 위해서는 작은수에서 큰수를 빼면됨\n",
    "* ' - ' 기준으로 괄호를 쳤을 때 최솟값이 됨.\n",
    "    * split('-') 으로하면 ' - ' 기준으로 문자 나뉨"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-35"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s=55-(50+40)\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55-50+40-30+20\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['55', '50+40', '30+20']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=input().split('-')\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['50', '40']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[1].split('+')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[55]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 숫자 하나만있을경우\n",
    "[int(x) for x in a[0].split('+')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[50, 40]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 숫자와 '+' 문자 둘다있을경우\n",
    "[int(x) for x in a[1].split('+')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "90"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 합계\n",
    "sum([int(x) for x in a[1].split('+')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[55, 90, 50]\n"
     ]
    }
   ],
   "source": [
    "# '-' 를 기준으로 양수만 더한값 리스트\n",
    "num=[]\n",
    "for i in range(len(a)):\n",
    "    num.append(sum([int(x) for x in a[i].split('+')]))\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-85\n"
     ]
    }
   ],
   "source": [
    "num=[]\n",
    "for i in range(len(a)):\n",
    "    num.append(sum([int(x) for x in a[i].split('+')]))\n",
    "\n",
    "answer=num[0]\n",
    "for j in range(1,len(num)):  # j=1,2\n",
    "    answer=answer-num[j]\n",
    "print(answer)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-------------------------------------------------------\n",
    "#### 수현's 최종코드\n",
    "* Point !!\n",
    "    * '-' 를 기준으로 split() 함수로 식을 분리한다는것이 첫번째 포인트\n",
    "    * 그다음 '+' 를 기준으로 다시 split() 으로 또 분리해서 덧셈연산을 하는것이 두번째 포인트"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55-50+40-30+20\n",
      "-85\n"
     ]
    }
   ],
   "source": [
    "a=input().split('-')\n",
    "num=[]\n",
    "for i in range(len(a)):\n",
    "    num.append(sum([int(x) for x in a[i].split('+')]))\n",
    "    \n",
    "answer=num[0]\n",
    "for j in range(1,len(num)):  # j=1,2\n",
    "    answer=answer-num[j]\n",
    "print(answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "suhyun2",
   "language": "python",
   "name": "suhyun2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
