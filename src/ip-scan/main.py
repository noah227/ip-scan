from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from typing import Tuple

from ping3 import ping


class IpScanner:
    def __init__(self, threadLimit=255, timeout=None):
        self.result = []
        self.threadLimit = threadLimit
        self.timeout = timeout
        pass

    @staticmethod
    def createIpPool(rangeStart: Tuple[int, int, int, int], rangeEnd: Tuple[int, int, int, int]):
        sa, sb, sc, sd = rangeStart
        ea, eb, ec, ed = rangeEnd
        return (
            f"{a}.{b}.{c}.{d}"
            for a in range(sa, ea + 1)
            for b in range(sb, eb + 1)
            for c in range(sc, ec + 1)
            for d in range(sd, ed + 1)
        )
        pass

    def __pingAddress(self, address):
        ret = ping(address)
        self.result.append([address, True if isinstance(ret, float) else False])

    def scanList(self, addressList):
        """
        :param addressList: A simple ip str list or generator.
        :return:
        """
        executor = ThreadPoolExecutor(max_workers=self.threadLimit)
        taskList = [executor.submit(self.__pingAddress, address) for address in addressList]
        wait(taskList, timeout=self.timeout, return_when=ALL_COMPLETED)
        self.result.sort()
        return self.result
        pass

    def scanRange(self, rangeStart: Tuple[int, int, int, int], rangeEnd: Tuple[int, int, int, int]):
        return self.scanList(self.createIpPool(rangeStart, rangeEnd))
        pass


if __name__ == "__main__":
    # result1 = IpScanner().scanList(["192.168.1.100", "192.168.1.200"])
    # print(result1)

    # this will scan ip from 200 to 202 (202 is included)
    result = IpScanner().scanRange((192, 168, 1, 200), (192, 168, 1, 202))
    print(result)
    # result = IpScanner().scanList(["192.168.1.100", "192.168.1.200"])
    # addressList = [f"192.168.1.{i}" for i in range(101, 103 + 1)]
    # result2 = IpScanner().scanList(addressList)
    # print(result2)
    pass
