class Solution:
    def __init__(self):
        self.min_cost = 99999999999

    def minimise_loss_recursive(self, wt_array, cst_array, cap, i):
        if i < 0:
            # if cap == 0:
            return 99999999


        print(f'i {i}')
        if wt_array[i] < cap:
            return min(cst_array[i] - self.minimise_loss_recursive(wt_array, cst_array, cap - wt_array[i], i), self.minimise_loss_recursive(wt_array, cst_array, cap, i-1))

        return self.minimise_loss_recursive(wt_array, cst_array, cap, i-1)

    def minimise_loss(self, weight_array, cost_array, capacity):
        ans = self.minimise_loss_recursive(weight_array, cost_array, capacity, len(weight_array)-1)
        print(f'ans is {ans}')


if __name__ == '__main__':
    w_array = [2, 1, 3]
    cst_array = [2, 5, 3]
    capa = 2
    obj = Solution()
    ans = obj.minimise_loss(w_array, cst_array, capa)