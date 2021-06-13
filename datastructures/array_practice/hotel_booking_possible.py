def hotel_booking_possible(arrive, depart, K):
    n = len(arrive)

    ans = []
    for i in range(n):
        ans.append((arrive[i], 1))
        ans.append((depart[i], 0))

    ans = sorted(ans, key=lambda x: x[0])
    curr_active = max_active = 0

    for i in ans:
        if i[1] == 1:
            curr_active += 1
            max_active = max(curr_active, max_active)
        else:
            curr_active -= 1

    return K >= max_active
