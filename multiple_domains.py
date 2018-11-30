# -*- coding: utf-8 -*-
# author: Tiancheng Zhao
from simdial.domain import Domain, DomainSpec
from simdial.generator import Generator
from simdial import complexity
import string


class RestSpec(DomainSpec):
    name = "restaurant"
    greet = "賃貸住宅検索システムです。"
    nlg_spec = {"loc": {"inform": ["%sがいいです。", "%s.", "%sに興味があります。", "%sです。", "%sをおねがいします。"],
                        "request": ["どこらへんがいいですか?", "場所はどこらへんを考えていますか?"]},

                "food_pref": {"inform": ["%sがいいです。", "%sです。", "%sが食べれるレストランがいいです。", "%s。"],
                              "request": ["何が食べたいですか。", "どんなレストランがいいですか。"]},

                "open": {"inform": ["そのレストランが開いているかは%s。", "ちょうどいま%s"],
                         "request": ["開いているか教えて.", "何時からやってますか?"],
                         "yn_question": {'open': ["そのレストランは開いてますか?"],
                                         'closed': ["閉まってる?"]
                                         }},

                "parking": {"inform": ["そのレストランの駐車場は%s.", "ここには%s."],
                            "request": ["駐車場はありますか?.", "車を停めるのは楽ですか?"],
                            "yn_question": {'street parking': ["道に停めることはできますか?"],
                                            "valet parking": ["専用の駐車場はありますか?"]
                                            }},

                "price": {"inform": ["そのレストランの値段は%s", "値段は%s."],
                          "request": ["平均的な値段は?", "どれくらい高いですか?"],
                          "yn_question": {'expensive': ["高いですか?"],
                                          'moderate': ["妥当な値段ですか?"],
                                          'cheap': ["安いですか?"]
                                          }},

                "default": {"inform": ["レストラン%sがおすすめです。"],
                            "request": ["レストランを探しています。",
                                        "おすすめのレストランは？",
                                        "レストランを推薦して。"]}
                }

    usr_slots = [("loc", "location city", ["っｓ", "New York", "Boston", "Seattle",
                                           "Los Angeles", "San Francisco", "San Jose",
                                           "Philadelphia", "Washington DC", "Austin"]),
                 ("food_pref", "food preference", ["Thai", "Chinese", "Korean", "Japanese",
                                                   "American", "Italian", "Indian", "French",
                                                   "Greek", "Mexican", "Russian", "Hawaiian"])]

    sys_slots = [("open", "if it's open now", ["open", "closed"]),
                 ("price", "average price per person", ["cheap", "moderate", "expensive"]),
                 ("parking", "if it has parking", ["street parking", "valet parking", "no parking"])]

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

