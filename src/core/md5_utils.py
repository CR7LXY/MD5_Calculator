import hashlib


def calc_string_md5(content: str) -> str:
    """计算字符串MD5（支持MAC地址）"""
    md5_obj = hashlib.md5()
    md5_obj.update(content.encode("utf-8"))
    return md5_obj.hexdigest().upper()


def calc_file_md5(file_path: str) -> str:
    """计算文件MD5（分块读取优化大文件）[1,4](@ref)"""
    md5_obj = hashlib.md5()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(8192)  # 分块读取避免内存溢出
            if not chunk:
                break
            md5_obj.update(chunk)
    return md5_obj.hexdigest().upper()

