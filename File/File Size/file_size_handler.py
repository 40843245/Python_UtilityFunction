class FileSizeHandler():
   class Format():
    """
	Description:
    	Scale bytes to its proper byte format.
	Paramater:
   		b:unformatted size.
    Returned Value:
		Return size as a string that has proper byte format (such as 1.5GB)
    Example:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    @staticmethod
    def format(b, factor=1024, suffix="B") -> str:
     for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
       if b < factor:
        return f"{b:.2f}{unit}{suffix}"
       b /= factor
     return f"{b:.2f}Y{suffix}"