# 在列表里查找能被2和3整除的数
# 方法一（结果不对 36没被删除）Reason:迭代一个数组时，不能删除它里面的元素。因为迭代的时候，用的是list.next().
# 如果删除了list里面的元素 next算出来的结果就不同了

# 你可以认为迭代的时候  是按照list的索引迭代的  比如你each取到了 第10个元素  你删除了一个元素
# 这个时候 list里面元素的下标都发生了变化了
# 因为少了一个元素 被删除后面的元素会往前移动  而指针没动   当再次执行循环的时候 就会跳过去一个元素
nums = [1, 2, 4, 3, 12, 6, 7, 8, 9, 10, 24, 36, 12]
for i in nums:
    if i % 2 == 0 and i % 3 == 0:
        nums.remove(i)
print(nums)

# 方法二 (深拷贝？)
nums1 = [1, 2, 4, 3, 12, 6, 7, 8, 9, 10, 24, 36, 12]
nums2 = nums1[:]
for i in nums1:
    if i % 2 == 0 and i % 3 == 0:
        nums2.remove(i)
        nums1 = nums2
print(nums1)

# 方法三 老公的想法
nums1 = []
for each in range(36):
    nums1.append(each + 1)
print(nums1)
for each in nums1:
    if each % 2 == 0 and each % 3 == 0:
        nums1.remove(each)
print(nums1)
