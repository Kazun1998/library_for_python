## セグメント木

* セグメント木
    * `Segment_Tree(L,calc,unit,index)`: 単位元が`unit`, 二項演算が`calc`であるモノイド上で, 初期値が $L$ , 先頭インデックスが`index`であるセグメント木を生成する.
    * `get(k, index=1)`: セグメント木の第 $k$ 要素を得る.
    * `update(k, x, index=1)`: セグメント木の第 $k$ 要素を $x$ に変更する.
    * `product(From,To,index=1,left_closed=True,right_closed=True)`: 第 ${\tt From}$ 要素から第 ${\tt To}$ 要素までの総積を求める (`left_closed`, `right_closed` でそれぞれ左端と右端が閉区間か開区間かどうかを表す.)
    * `all_product()`: 全ての要素の総積を求める.
    * `max_right(left, cond, index=1)`: 以下2つの条件を共に満たす $x$ の一つを返す.
        1. x=left or cond(data[left]\*data[left+1]*...\*d[x-1]):真
        2. x=N+index or cond(data[left]\*data[left+1]*...\*data[x]):偽
    * `min_left(right, cond, index=1)`: 以下2つの条件を共に満たす $y$ の一つを返す.
        1. y=right or cond(data[y]\*data[y+1]*...\*d[right-1]):真
        2. y=index or cond(data[y-1]\*data[y]\*data[y+1]*...\*data[right]):偽