from LAC import LAC

lac = LAC(mode='lac')
# sentence = 'e5fa5e8a5f1c0f2e3n153di6E1VT34u8VvmeQ-Sl 王江 代码整洁，算法基础好，工程能力强，架构意识努力中  男  25  本科  上海  3年经验  17811941572  wang0624@foxmail.com'
sentence = '百度在线网络技术（北京）有限公司'
lac_result = lac.run(sentence)
print(lac_result)
