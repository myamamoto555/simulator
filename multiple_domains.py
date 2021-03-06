# -*- coding: utf-8 -*-
# author: Tiancheng Zhao
from simdial.domain import Domain, DomainSpec
from simdial.generator import Generator
from simdial import complexity
import string


class EstateSpec(DomainSpec):
    name = "estate"
    greet = "賃貸住宅検索システムです。"
    nlg_spec = {"loc": {"inform": ["%sがいいです。", "%s", "%sです。", "%sでおねがいします。"],
                        "request": ["最寄り駅の希望を教えて下さい", "最寄りの駅はどこらへんを考えていますか?"]},
                "price": {"inform": ["%s以下だと嬉しいです。", "だいたい%sくらいで考えています。"],
                          "request": ["家賃はどれくらいを想定していますか？"]},
                "people": {"inform": ["%sです", "%s"],
                           "request": ["何人でお住まいの予定ですか。"]}
                }

    usr_slots = [("loc", "location city", ["新宿", "大崎", "品川"], ["新宿駅", "大崎駅", "品川駅"]),
                 ("price", "price range", ["5万円", "8万円", "10万円"], ["50000", "80000", "100000"]),
                 ("people", "the number of people", ["1人", "2人", "3人", "4人"], ["1", "2", "3", "4"])
                 ]

    sys_slots = []

    db_size = 100


if __name__ == "__main__":
    # pipeline here
    # generate a fix 500 test set and 5000 training set.
    # generate them separately so the model can choose a subset for train and
    # test on all the test set to see generalization.

    test_size = 500
    #train_size = 2000
    gen_bot = Generator()

    estate_spec = EstateSpec()

    # restaurant
    gen_bot.gen_corpus("test", estate_spec, complexity.CleanSpec, test_size)
    #gen_bot.gen_corpus("test", estate_spec, complexity.MixSpec, test_size)
    #gen_bot.gen_corpus("train", rest_spec, complexity.CleanSpec, train_size)
    #gen_bot.gen_corpus("train", rest_spec, complexity.MixSpec, train_size)

