from bosonnlp import BosonNLP
import os
nlp = BosonNLP(os.environ['BOSON_API_TOKEN'])
nlp.ner('杨超越在1998年7月31日出生于江苏省盐城市大丰区。', sensitivity=2)