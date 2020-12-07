interval_insert(T,x)
interval_delete(T,x)
interval_search(T,i)

#もとはrb_tree, keyは下端点,
#補強として区間int(x)を保持
#補強としてmax(x):xを根とする木の上端点の最大値
#挿入削除がO(logn)でできることは例の定理よりわかる
#searchは？
