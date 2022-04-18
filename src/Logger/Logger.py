from asyncio.log import logger


def decode_encode(code:str)->str:
    
    def ansi_encoder(esc_code: str) -> str: return f"\033[{esc_code}m"

    match code:
        case "-clc": #Removes all formatting.
            return ansi_encoder("0")
        case "-b"|"-B": #Sets Text to Bold.
            return ansi_encoder("1")
        case "-i"|"-I": #Sets Text to Italic.
            return ansi_encoder("3") 
        case "-u"|"-U": #Sets Text to Underlined.
            return ansi_encoder("4")
        case "-s"|"-S": #Sets Text to Strikethrough.
            return ansi_encoder("9")
        case "-gr"|"-GR": #Sets font color to Gray.
            return ansi_encoder("90")
        case "-r"|"-R": #Sets font color to Red.
            return ansi_encoder("91")
        case "-g"|"-G": #Sets font color to Green.
            return ansi_encoder("92")
        case "-y"|"-Y": #Sets font color to Yellow.
            return ansi_encoder("93")
        case "-c"|"-C": #Sets font color to Cyan.
            return ansi_encoder("96")
        case _: #Wildcard
            return ""

def sanitize(msg:list) -> list:
    sanitized_msg = []
    for word in msg:
        match word:
            case '"':
                sanitized_msg.append("\"")
            case "'":
                sanitized_msg.append("\'")
            case "\n"|"\t"|"\r"|"\b"|"\f"|"\\":
                continue
            case _:
                sanitized_msg.append(str(word))
    
    return sanitized_msg, len(sanitized_msg)

class Logger:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def Log(input:str = None):
        if input is None: input = ""

        msg_list, msg_length = sanitize(input.split(" "))

        if msg_length <=1:
            msg_type,msg = ("WARN","No Message Provided for Logger. Double-check input.")
        else:
            msg_type = msg_list.pop(0).capitalize()
            msg = " ".join([m for m in msg_list if "-" not in m])
            params_list = [p for p in msg_list if "-" in p]

        dc_ec = decode_encode
        match msg_type:
            case "WARN":
                header = f'{dc_ec("-b")}{dc_ec("-u")}{dc_ec("-y")}{msg_type}{dc_ec("-clc")}{dc_ec("-y")}: '
            case "ERROR"|"ERR":
                header = f'{dc_ec("-b")}{dc_ec("-u")}{dc_ec("-r")}ERROR{dc_ec("-clc")}{dc_ec("-r")}: '
            case "PASS":
                header = f'{dc_ec("-b")}{dc_ec("-u")}{dc_ec("-g")}{msg_type}{dc_ec("-clc")}{dc_ec("-g")}: '
            case "OKAY"|"OK":
                header = f'{dc_ec("-b")}{dc_ec("-u")}{dc_ec("-c")}OK{dc_ec("-clc")}{dc_ec("-c")}: '
            case "DEPRICATED"|"DEPR":
                header = f'{dc_ec("-b")}{dc_ec("-u")}{dc_ec("-gr")}DEPRICATED{dc_ec("-clc")}{dc_ec("-gr")}{dc_ec("-s")}: '
            case _:
                header = f'{dc_ec("-b")}{dc_ec("-u")}{str(msg_type)}{dc_ec("-clc")}: '
        
        params = ""
        for param in params_list:
            params += dc_ec(param)

        out = f'{header}{params}{msg}{dc_ec("-clc")}'

        print(out)

if __name__ == "__main__":
    from sys import version_info, exit
    if version_info <(3,10):
        print("Your current Python version is: {version_info[0]}.{version_info[1]}.\n Please upgrade to version 3.10 or higher.")
    else:
        print("A Basic Logging Module with Formatting.")
    exit()