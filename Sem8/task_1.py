# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

fruits_list1 = ['яблоко', 'банан', 'груша', 'киви', 'апельсин']
fruits_list2 = ['груша', 'киви', 'ананас', 'манго', 'яблоко']

common_fruits = [fruit for fruit in fruits_list1 if fruit in fruits_list2]
print(common_fruits)