import zipfile


def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack
	"""
	zipfilename = 'clues.zip'

	zip_file = zipfile.ZipFile(zipfilename)

	for k in range(10^6):
		password = k
		try:
			zip_file.extractall(pwd=password)
		except:
			pass

	print(f'Password found: {k}' )

if __name__ == '__main__':
	main()

