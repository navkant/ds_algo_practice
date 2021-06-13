def get_subset(start, input, output, ans):
    # print(f'start: {start}: input: {input[start:]} output: {output}, ans: {ans}')
    if output not in ans:
        ans.append(output)
    if start == len(input):
        return
    get_subset(start+1, input, output, ans)
    output = output + input[start]
    get_subset(start+1, input, output, ans)
    return ans


if __name__ == '__main__':
    string = 'abcbacabc'
    n = len(string)
    input = string
    output = ''
    ans = list()
    a = get_subset(0, input, output, ans)
    print(a)

