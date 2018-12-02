# -*- coding: utf-8 -*-
# author: Tiancheng Zhao
from simdial.domain import Domain, DomainSpec
from simdial.generator import Generator
from simdial import complexity
import string


class RestSpec(DomainSpec):
    name = "restaurant"
    greet = "賃貸住宅検索システムです。"
    nlg_spec = {"loc": {"inform": ["%sがいいです。", "%s", "%sです。", "%sでおねがいします。"],
                        "request": ["どこらへんがいいですか?", "場所はどこらへんを考えていますか?"]},
                "price": {"inform": ["%s以下だと嬉しいです。", "だいたい%sくらいで考えています。"],
                          "request": ["家賃はどれくらいを想定していますか？"]}
                }

    usr_slots = [("loc", "location city", ["新宿", "大崎", "品川"]),
                 ("price", "price range", ["5万円", "8万円", "10万円"])]

    sys_slots = []

    db_size = 100


if __name__ == "__main__":
    # pipeline here
    # generate a fix 500 test set and 5000 training set.
    # generate them separately so the model can choose a subset for train and
    # test on all the test set to see generalization.

    test_size = 500
    train_size = 2000
    gen_bot = Generator()

    rest_spec = RestSpec()

    # restaurant
    gen_bot.gen_corpus("test", rest_spec, complexity.CleanSpec, test_size)
    gen_bot.gen_corpus("test", rest_spec, complexity.MixSpec, test_size)
    gen_bot.gen_corpus("train", rest_spec, complexity.CleanSpec, train_size)
    gen_bot.gen_corpus("train", rest_spec, complexity.MixSpec, train_size)

