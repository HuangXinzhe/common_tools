from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import time

ner_pipeline = pipeline(Tasks.named_entity_recognition, 'damo/nlp_raner_named-entity-recognition_chinese-base-resume')

start_time = time.time()
result = ner_pipeline('百度在线网络技术（北京）有限公司 常建良 男 java工程师 百度 java')
end_time = time.time()

print(result)
print(end_time-start_time)