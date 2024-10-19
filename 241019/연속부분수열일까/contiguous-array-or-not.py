import sys

# 정수 n1과 n2를 입력받습니다.
n1, n2 = tuple(map(int, input().split()))

# arr1을 입력받습니다.
arr1 = list(map(int, input().split()))

# arr2를 입력받습니다.
arr2 = list(map(int, input().split()))
	
# arr2이 arr1의 연속부분수열인지 확인합니다.
for i in range(n1):
	# arr1의 i번 index부터의 수열이 arr2와 완전히 일치하는지 확인합니다.
	# 즉, arr1[i] == arr2[0], arr1[i+1] == arr2[1]...이 성립하는지 확인합니다.
	# success : arr1의 i번 index부터의 수열이 arr2와 완전히 일치할때만 true, 그 외 false
	success = True
	
	for j in range(n2):
		# arr1의 index가 범위 밖으로 벗어날때
		if i + j >= n1:
			success = False
			break

		# arr1과 arr2가 일치하지 않을때
		if arr1[i + j] != arr2[j]:
			success = False
			break
		
	# 완전히 일치할 경우, arr2는 arr1의 연속부분수열이 맞습니다.
	# 구현의 편의를 위해 sys라이브러리를 가져와 sys.exit()으로 프로그램을 강제 종료하였습니다.
	if success:
		print("Yes")
		sys.exit()
	
# 완전히 일치하는 경우가 하나도 없을 경우, arr2는 arr1의 연속부분수열이 아닙니다.
print("No")