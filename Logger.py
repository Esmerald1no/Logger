

def ansi_encoder(esc_code: str) -> str: return f"\033[{esc_code}m"

def decode_encode(code:str)->str:
        match code:
            case "-b"|"-B":
                return ansi_encoder("1")
            case "-i"|"-I":
                return ansi_encoder("3")
            case "-u"|"-U":
                return ansi_encoder("4")
            case "-clc":
                return ansi_encoder("0")
            case "-r"|"-R":
                return ansi_encoder("91")
            case "-g"|"-G":
                return ansi_encoder("92")
            case "-y"|"-Y":
                return ansi_encoder("93")
            case "-c"|"-C":
                return ansi_encoder("96")
            case _:
                return ""


class Logger:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def Log(input:str):
        msg_list = input.split(" ")
        msg_type = msg_list.pop(0)
        msg = " ".join([m for m in msg_list if "-" not in m])
        params = [p for p in msg_list if "-" in p]

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
            case _:
                header = f'{dc_ec("-b")}{dc_ec("-u")}{str(msg_type)}{dc_ec("-clc")}: '

        out = f'{header}{dc_ec(params)}{msg}{dc_ec("-clc")}'

        print(out)
