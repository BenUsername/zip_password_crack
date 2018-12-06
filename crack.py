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
			password = 'Password found: %s' % password
		except:
			pass

	print(password)

if __name__ == '__main__':
	main()
