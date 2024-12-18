"""
Code Written by Jackson L. Davis

This class is for a computer player that plays as the codebreaker in the board game "Mastermind."
The computer player will use Donald Knuth's five-guess algorithm to break the code.
Information about this algorithm can be found here:
https://en.wikipedia.org/wiki/Mastermind_(board_game)#Worst_case:_Five-guess_algorithm
"""

from board import Board
import random as rand
import time as time


class ComputerPlayer:
    def __init__(self, board):
        """
        Constructor method for the computer player
        :param board: a decoding board that the computer player sends guesses to
        """
        self.__board = board
        self.__unused_codes = ["1111", "1112", "1113", "1114", "1115", "1116",
                               "1121", "1122", "1123", "1124", "1125", "1126",
                               "1131", "1132", "1133", "1134", "1135", "1136",
                               "1141", "1142", "1143", "1144", "1145", "1146",
                               "1151", "1152", "1153", "1154", "1155", "1156",
                               "1161", "1162", "1163", "1164", "1165", "1166",
                               "1211", "1212", "1213", "1214", "1215", "1216",
                               "1221", "1222", "1223", "1224", "1225", "1226",
                               "1231", "1232", "1233", "1234", "1235", "1236",
                               "1241", "1242", "1243", "1244", "1245", "1246",
                               "1251", "1252", "1253", "1254", "1255", "1256",
                               "1261", "1262", "1263", "1264", "1265", "1266",
                               "1311", "1312", "1313", "1314", "1315", "1316",
                               "1321", "1322", "1323", "1324", "1325", "1326",
                               "1331", "1332", "1333", "1334", "1335", "1336",
                               "1341", "1342", "1343", "1344", "1345", "1346",
                               "1351", "1352", "1353", "1354", "1355", "1356",
                               "1361", "1362", "1363", "1364", "1365", "1366",
                               "1411", "1412", "1413", "1414", "1415", "1416",
                               "1421", "1422", "1423", "1424", "1425", "1426",
                               "1431", "1432", "1433", "1434", "1435", "1436",
                               "1441", "1442", "1443", "1444", "1445", "1446",
                               "1451", "1452", "1453", "1454", "1455", "1456",
                               "1461", "1462", "1463", "1464", "1465", "1466",
                               "1511", "1512", "1513", "1514", "1515", "1516",
                               "1521", "1522", "1523", "1524", "1525", "1526",
                               "1531", "1532", "1533", "1534", "1535", "1536",
                               "1541", "1542", "1543", "1544", "1545", "1546",
                               "1551", "1552", "1553", "1554", "1555", "1556",
                               "1561", "1562", "1563", "1564", "1565", "1566",
                               "1611", "1612", "1613", "1614", "1615", "1616",
                               "1621", "1622", "1623", "1624", "1625", "1626",
                               "1631", "1632", "1633", "1634", "1635", "1636",
                               "1641", "1642", "1643", "1644", "1645", "1646",
                               "1651", "1652", "1653", "1654", "1655", "1656",
                               "1661", "1662", "1663", "1664", "1665", "1666",
                               "2111", "2112", "2113", "2114", "2115", "2116",
                               "2121", "2122", "2123", "2124", "2125", "2126",
                               "2131", "2132", "2133", "2134", "2135", "2136",
                               "2141", "2142", "2143", "2144", "2145", "2146",
                               "2151", "2152", "2153", "2154", "2155", "2156",
                               "2161", "2162", "2163", "2164", "2165", "2166",
                               "2211", "2212", "2213", "2214", "2215", "2216",
                               "2221", "2222", "2223", "2224", "2225", "2226",
                               "2231", "2232", "2233", "2234", "2235", "2236",
                               "2241", "2242", "2243", "2244", "2245", "2246",
                               "2251", "2252", "2253", "2254", "2255", "2256",
                               "2261", "2262", "2263", "2264", "2265", "2266",
                               "2311", "2312", "2313", "2314", "2315", "2316",
                               "2321", "2322", "2323", "2324", "2325", "2326",
                               "2331", "2332", "2333", "2334", "2335", "2336",
                               "2341", "2342", "2343", "2344", "2345", "2346",
                               "2351", "2352", "2353", "2354", "2355", "2356",
                               "2361", "2362", "2363", "2364", "2365", "2366",
                               "2411", "2412", "2413", "2414", "2415", "2416",
                               "2421", "2422", "2423", "2424", "2425", "2426",
                               "2431", "2432", "2433", "2434", "2435", "2436",
                               "2441", "2442", "2443", "2444", "2445", "2446",
                               "2451", "2452", "2453", "2454", "2455", "2456",
                               "2461", "2462", "2463", "2464", "2465", "2466",
                               "2511", "2512", "2513", "2514", "2515", "2516",
                               "2521", "2522", "2523", "2524", "2525", "2526",
                               "2531", "2532", "2533", "2534", "2535", "2536",
                               "2541", "2542", "2543", "2544", "2545", "2546",
                               "2551", "2552", "2553", "2554", "2555", "2556",
                               "2561", "2562", "2563", "2564", "2565", "2566",
                               "2611", "2612", "2613", "2614", "2615", "2616",
                               "2621", "2622", "2623", "2624", "2625", "2626",
                               "2631", "2632", "2633", "2634", "2635", "2636",
                               "2641", "2642", "2643", "2644", "2645", "2646",
                               "2651", "2652", "2653", "2654", "2655", "2656",
                               "2661", "2662", "2663", "2664", "2665", "2666",
                               "3111", "3112", "3113", "3114", "3115", "3116",
                               "3121", "3122", "3123", "3124", "3125", "3126",
                               "3131", "3132", "3133", "3134", "3135", "3136",
                               "3141", "3142", "3143", "3144", "3145", "3146",
                               "3151", "3152", "3153", "3154", "3155", "3156",
                               "3161", "3162", "3163", "3164", "3165", "3166",
                               "3211", "3212", "3213", "3214", "3215", "3216",
                               "3221", "3222", "3223", "3224", "3225", "3226",
                               "3231", "3232", "3233", "3234", "3235", "3236",
                               "3241", "3242", "3243", "3244", "3245", "3246",
                               "3251", "3252", "3253", "3254", "3255", "3256",
                               "3261", "3262", "3263", "3264", "3265", "3266",
                               "3311", "3312", "3313", "3314", "3315", "3316",
                               "3321", "3322", "3323", "3324", "3325", "3326",
                               "3331", "3332", "3333", "3334", "3335", "3336",
                               "3341", "3342", "3343", "3344", "3345", "3346",
                               "3351", "3352", "3353", "3354", "3355", "3356",
                               "3361", "3362", "3363", "3364", "3365", "3366",
                               "3411", "3412", "3413", "3414", "3415", "3416",
                               "3421", "3422", "3423", "3424", "3425", "3426",
                               "3431", "3432", "3433", "3434", "3435", "3436",
                               "3441", "3442", "3443", "3444", "3445", "3446",
                               "3451", "3452", "3453", "3454", "3455", "3456",
                               "3461", "3462", "3463", "3464", "3465", "3466",
                               "3511", "3512", "3513", "3514", "3515", "3516",
                               "3521", "3522", "3523", "3524", "3525", "3526",
                               "3531", "3532", "3533", "3534", "3535", "3536",
                               "3541", "3542", "3543", "3544", "3545", "3546",
                               "3551", "3552", "3553", "3554", "3555", "3556",
                               "3561", "3562", "3563", "3564", "3565", "3566",
                               "3611", "3612", "3613", "3614", "3615", "3616",
                               "3621", "3622", "3623", "3624", "3625", "3626",
                               "3631", "3632", "3633", "3634", "3635", "3636",
                               "3641", "3642", "3643", "3644", "3645", "3646",
                               "3651", "3652", "3653", "3654", "3655", "3656",
                               "3661", "3662", "3663", "3664", "3665", "3666",
                               "4111", "4112", "4113", "4114", "4115", "4116",
                               "4121", "4122", "4123", "4124", "4125", "4126",
                               "4131", "4132", "4133", "4134", "4135", "4136",
                               "4141", "4142", "4143", "4144", "4145", "4146",
                               "4151", "4152", "4153", "4154", "4155", "4156",
                               "4161", "4162", "4163", "4164", "4165", "4166",
                               "4211", "4212", "4213", "4214", "4215", "4216",
                               "4221", "4222", "4223", "4224", "4225", "4226",
                               "4231", "4232", "4233", "4234", "4235", "4236",
                               "4241", "4242", "4243", "4244", "4245", "4246",
                               "4251", "4252", "4253", "4254", "4255", "4256",
                               "4261", "4262", "4263", "4264", "4265", "4266",
                               "4311", "4312", "4313", "4314", "4315", "4316",
                               "4321", "4322", "4323", "4324", "4325", "4326",
                               "4331", "4332", "4333", "4334", "4335", "4336",
                               "4341", "4342", "4343", "4344", "4345", "4346",
                               "4351", "4352", "4353", "4354", "4355", "4356",
                               "4361", "4362", "4363", "4364", "4365", "4366",
                               "4411", "4412", "4413", "4414", "4415", "4416",
                               "4421", "4422", "4423", "4424", "4425", "4426",
                               "4431", "4432", "4433", "4434", "4435", "4436",
                               "4441", "4442", "4443", "4444", "4445", "4446",
                               "4451", "4452", "4453", "4454", "4455", "4456",
                               "4461", "4462", "4463", "4464", "4465", "4466",
                               "4511", "4512", "4513", "4514", "4515", "4516",
                               "4521", "4522", "4523", "4524", "4525", "4526",
                               "4531", "4532", "4533", "4534", "4535", "4536",
                               "4541", "4542", "4543", "4544", "4545", "4546",
                               "4551", "4552", "4553", "4554", "4555", "4556",
                               "4561", "4562", "4563", "4564", "4565", "4566",
                               "4611", "4612", "4613", "4614", "4615", "4616",
                               "4621", "4622", "4623", "4624", "4625", "4626",
                               "4631", "4632", "4633", "4634", "4635", "4636",
                               "4641", "4642", "4643", "4644", "4645", "4646",
                               "4651", "4652", "4653", "4654", "4655", "4656",
                               "4661", "4662", "4663", "4664", "4665", "4666",
                               "5111", "5112", "5113", "5114", "5115", "5116",
                               "5121", "5122", "5123", "5124", "5125", "5126",
                               "5131", "5132", "5133", "5134", "5135", "5136",
                               "5141", "5142", "5143", "5144", "5145", "5146",
                               "5151", "5152", "5153", "5154", "5155", "5156",
                               "5161", "5162", "5163", "5164", "5165", "5166",
                               "5211", "5212", "5213", "5214", "5215", "5216",
                               "5221", "5222", "5223", "5224", "5225", "5226",
                               "5231", "5232", "5233", "5234", "5235", "5236",
                               "5241", "5242", "5243", "5244", "5245", "5246",
                               "5251", "5252", "5253", "5254", "5255", "5256",
                               "5261", "5262", "5263", "5264", "5265", "5266",
                               "5311", "5312", "5313", "5314", "5315", "5316",
                               "5321", "5322", "5323", "5324", "5325", "5326",
                               "5331", "5332", "5333", "5334", "5335", "5336",
                               "5341", "5342", "5343", "5344", "5345", "5346",
                               "5351", "5352", "5353", "5354", "5355", "5356",
                               "5361", "5362", "5363", "5364", "5365", "5366",
                               "5411", "5412", "5413", "5414", "5415", "5416",
                               "5421", "5422", "5423", "5424", "5425", "5426",
                               "5431", "5432", "5433", "5434", "5435", "5436",
                               "5441", "5442", "5443", "5444", "5445", "5446",
                               "5451", "5452", "5453", "5454", "5455", "5456",
                               "5461", "5462", "5463", "5464", "5465", "5466",
                               "5511", "5512", "5513", "5514", "5515", "5516",
                               "5521", "5522", "5523", "5524", "5525", "5526",
                               "5531", "5532", "5533", "5534", "5535", "5536",
                               "5541", "5542", "5543", "5544", "5545", "5546",
                               "5551", "5552", "5553", "5554", "5555", "5556",
                               "5561", "5562", "5563", "5564", "5565", "5566",
                               "5611", "5612", "5613", "5614", "5615", "5616",
                               "5621", "5622", "5623", "5624", "5625", "5626",
                               "5631", "5632", "5633", "5634", "5635", "5636",
                               "5641", "5642", "5643", "5644", "5645", "5646",
                               "5651", "5652", "5653", "5654", "5655", "5656",
                               "5661", "5662", "5663", "5664", "5665", "5666",
                               "6111", "6112", "6113", "6114", "6115", "6116",
                               "6121", "6122", "6123", "6124", "6125", "6126",
                               "6131", "6132", "6133", "6134", "6135", "6136",
                               "6141", "6142", "6143", "6144", "6145", "6146",
                               "6151", "6152", "6153", "6154", "6155", "6156",
                               "6161", "6162", "6163", "6164", "6165", "6166",
                               "6211", "6212", "6213", "6214", "6215", "6216",
                               "6221", "6222", "6223", "6224", "6225", "6226",
                               "6231", "6232", "6233", "6234", "6235", "6236",
                               "6241", "6242", "6243", "6244", "6245", "6246",
                               "6251", "6252", "6253", "6254", "6255", "6256",
                               "6261", "6262", "6263", "6264", "6265", "6266",
                               "6311", "6312", "6313", "6314", "6315", "6316",
                               "6321", "6322", "6323", "6324", "6325", "6326",
                               "6331", "6332", "6333", "6334", "6335", "6336",
                               "6341", "6342", "6343", "6344", "6345", "6346",
                               "6351", "6352", "6353", "6354", "6355", "6356",
                               "6361", "6362", "6363", "6364", "6365", "6366",
                               "6411", "6412", "6413", "6414", "6415", "6416",
                               "6421", "6422", "6423", "6424", "6425", "6426",
                               "6431", "6432", "6433", "6434", "6435", "6436",
                               "6441", "6442", "6443", "6444", "6445", "6446",
                               "6451", "6452", "6453", "6454", "6455", "6456",
                               "6461", "6462", "6463", "6464", "6465", "6466",
                               "6511", "6512", "6513", "6514", "6515", "6516",
                               "6521", "6522", "6523", "6524", "6525", "6526",
                               "6531", "6532", "6533", "6534", "6535", "6536",
                               "6541", "6542", "6543", "6544", "6545", "6546",
                               "6551", "6552", "6553", "6554", "6555", "6556",
                               "6561", "6562", "6563", "6564", "6565", "6566",
                               "6611", "6612", "6613", "6614", "6615", "6616",
                               "6621", "6622", "6623", "6624", "6625", "6626",
                               "6631", "6632", "6633", "6634", "6635", "6636",
                               "6641", "6642", "6643", "6644", "6645", "6646",
                               "6651", "6652", "6653", "6654", "6655", "6656",
                               "6661", "6662", "6663", "6664", "6665", "6666"]
        self.__possible_codes = self.__unused_codes.copy()
        self.__responses = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1),
                            (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0)]

    def solve(self):
        """
        Break the code by using Donald Knuth's five-guess algorithm.
        Note that solve() and the methods it uses do not access self.__board.code at any point.
        :postcond: each guess and response is printed to the console
        :return: the amount of time it took the computer to break the code
        """
        start_time = time.time()
        # initial guess: 1122
        guess = "1122"
        self.__unused_codes.remove(guess)
        self.__board.add_guess(guess)
        resp = self.__board.responses[-1]
        print(guess + " | " + str(resp))
        while not self.__board.solved and len(self.__board.guesses) < self.__board.max_guesses:
            if guess in self.__possible_codes:
                self.__possible_codes.remove(guess)
            else:
                pass
            # remove all codes that do not give the same response as resp
            for c in self.codes_to_remove(guess, resp):
                self.__possible_codes.remove(c)
            # make a next guess
            guess = self.next_guess()
            self.__unused_codes.remove(guess)
            self.__board.add_guess(guess)
            resp = self.__board.responses[-1]
            print(guess + " | " + str(resp))
        end_time = time.time()
        return end_time - start_time

    def codes_to_remove(self, guess, resp):
        """
        Make a list of codes that when given the parameter guess, do not give the same response as resp
        :param guess: the most recent guess
        :param resp: the most recent response
        :return: a list of codes to remove from self.__possible_codes
        """
        to_remove = []
        for c in self.__possible_codes:
            if self.simulate_response(c, guess) != resp:
                to_remove.append(c)
            else:
                pass
        return to_remove

    def number_of_codes_to_remove(self, guess, resp):
        """
        Find out how many codes can be removed from self.__possible_guesses given the parameters guess and resp
        :param guess: a code
        :param resp: a response
        :return: an integer representing how many codes can be removed from self.__possible_codes
        """
        to_remove = 0
        for c in self.__possible_codes:
            if self.simulate_response(c, guess) != resp:
                to_remove += 1
            else:
                pass
        return to_remove

    def simulate_response(self, sim_code, sim_guess):
        """
        Simulate a response based on a mock code and mock guess
        :param sim_code: a possible code that stands in as a code
        :param sim_guess: a guess for sim_code
        :return: the response for if sim_guess was a guess for sim_code
        """
        correct_colour_and_position = 0
        correct_colour_wrong_position = 0
        code_peg_taken = [False] * 4  # list to keep track of which pegs in the code are taken by a peg in the guess
        guess_peg_taken = [False] * 4  # list to keep track of which pegs in the guess are taken by a peg in the code

        # check for correct colour and position
        for i in range(4):
            if sim_guess[i] == sim_code[i]:
                correct_colour_and_position += 1
                code_peg_taken[i] = True
                guess_peg_taken[i] = True
            else:
                pass

        # check correct colour wrong position
        for j in range(4):
            if not guess_peg_taken[j]:
                for k in range(4):
                    if j != k:
                        if sim_guess[j] == sim_code[k] and not code_peg_taken[k]:
                            correct_colour_wrong_position += 1
                            code_peg_taken[k] = True
                            guess_peg_taken[j] = True
                            break
                    else:
                        pass
            else:
                pass

        return (correct_colour_and_position, correct_colour_wrong_position)

    def next_guess(self):
        """
        Use the minimax technique to choose a code in self.__unused_codes with the
        least worst score as the next guess.
        A response to a code is one of the responses in self.__responses,
        the score of a response is the number of codes in self.__possible_codes that are still possible after the
        response is known,
        and the score of a code is the worst (maximum) of all its response scores.
        From the set of unused codes with the best (minimum) score, select one of them as the next guess,
        choose a code from self.__possible_codes if possible, choose the code with the least numeric value
        (ex. 2345 is less than 3456).
        :return: a code that will be used as the next guess
        """
        best_score = len(self.__possible_codes)
        best_codes = []
        for c in self.__unused_codes:
            code_score = self.get_code_score(c)
            # modify best_score and best_codes if necessary
            if code_score < best_score:
                best_score = code_score
                best_codes.clear()
                best_codes.append(c)
            elif code_score == best_score:
                best_codes.append(c)
            else:
                pass
        # choose next guess, choose a code that is in self.__possible_codes if possible
        for best_code in best_codes:
            if best_code in self.__possible_codes:
                return best_code
            else:
                pass
        return best_codes[0]

    def get_code_score(self, code):
        """
        Get a code's score.
        A code's score is the worst (maximum) of all its response scores,
        a response score is the number of codes in self.__possible_codes that are still possible after a certain
        response is known,
        a response used for a response score is one of the responses in self.__responses.
        :param code: a code from self.__unused_codes
        :return: the code's score
        """
        worst_score = 0
        for r in self.__responses:
            resp_score = self.get_response_score(code, r)
            # modify worst_score if necessary
            if resp_score > worst_score:
                worst_score = resp_score
            else:
                pass
        return worst_score

    def get_response_score(self, code, resp):
        """
        Get a response score given a possible code and a specific response.
        The response's score is the number of codes in self.__possible_codes that are still possible after the
        parameter resp for the parameter code is known.
        :param code: a code from self.__unused codes
        :param resp: a response from self.__responses
        :return: the response score
        """
        return len(self.__possible_codes) - self.number_of_codes_to_remove(code, resp)


if __name__ == '__main__':
    print("Computer Player")
    solved_boards = 0
    unsolved_boards = 0

    # code for printing possible codes so that I do not have to type them myself
    # for i in range(1, 7):
    #    for j in range(1, 7):
    #        for k in range(1, 7):
    #            for l in range(1, 7):
    #                print("\"" + str(i) + str(j) + str(k) + str(l) + "\", ", end="")
    #            print()

    # set up example codes
    example_codes = ["1122", "1111", "1234", "6543", "5555", "2424", "6333", "2121", "4565", "6666"]
    for ec in example_codes:
        print("Code: " + ec)
        test_board = Board(ec)
        test_computer_player = ComputerPlayer(test_board)
        test_solve_time = test_computer_player.solve()
        if test_board.solved:
            print("Solved in " + str(test_solve_time) + " seconds.\n")
            solved_boards += 1
        else:
            print("Computer player did not successfully break the code\n")
            unsolved_boards += 1

    # set up random codes
    for a in range(10):
        random_code = ""
        for b in range(4):
            random_code += str(rand.randint(1, 6))
        print("Random code: " + random_code)
        random_board = Board(random_code)
        random_computer_player = ComputerPlayer(random_board)
        random_solve_time = random_computer_player.solve()
        if random_board.solved:
            print("Solved in " + str(random_solve_time) + " seconds.\n")
            solved_boards += 1
        else:
            print("Computer player did not successfully break the code\n")
            unsolved_boards += 1

    print("Number of solved boards: " + str(solved_boards))
    print("Number of unsolved boards: " + str(unsolved_boards))
