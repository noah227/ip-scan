# ip-scan
 
Scan if ip is available within specified range
 
# Installation
```shell
pip install ip-scan
```

# Usage
* import
```python
from ip_scan import IpScanner
```
* scan directly with a simple ip list or generator.
```python
result1 = IpScanner().scanList(["192.168.1.100", "192.168.1.200"])
print(result1)

addressList = [f"192.168.1.{i}" for i in range(101, 103 + 1)]
result2 = IpScanner().scanList(addressList)
print(result2)
```
```
# output:

# result1:
[['192.168.1.100', False], ['192.168.1.200', True]]

# result2:
[['192.168.1.101', False], ['192.168.1.102', False], ['192.168.1.103', False]]
```
* scan within range
```python
# this will scan ip from 200 to 202 (202 is included)
result = IpScanner().scanRange((192, 168, 1, 200), (192, 168, 1, 202))
print(result)
```
```
# output:
[['192.168.1.200', True], ['192.168.1.201', False], ['192.168.1.202', False]]
```

# Others

* Domain is supported though this pack mainly aims to ip range scan.

# License

Whatever you like.