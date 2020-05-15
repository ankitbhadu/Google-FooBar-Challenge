import base64
#Decode the message to base64 bytes and then do XOR of decoded bytes with username
MESSAGE = '''
GkkYHBdNBxsSQ1UNF0YJGQwVWkVEQUMWWFsNCwoOAUtFSFtEUlJEFQsOBBFKRURBQxBRUQ4cHxpT DlhIRg0bVEUECgILGEtFREFDFFRfCAsdDBlLDBxGRE8XEBQABwYXRQcMRkhVEEUADAkAAF1FSFtE UkRWBwtMRVQJBAcOQ1UNF0YZAgdVCR8=
'''
KEY = 'ankit.bhadu77'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))