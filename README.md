# pyrouge-AND-rouge-Configure
教你如何在windows系统上进行文本摘要ROUGE测评！
   rouge作为NLP 文本摘要领域最为重要的评测手段，rouge受到了机器翻译评价方法BLEU的启发，不同之处在于采用了召回率作为指标。本文介绍了如何在windows系统配置rouge。
  
  Step1:
首先，下载Strawberry Perl，选择较新版本，安装到D:\下，找到并运行perl中组件CPAN Client，打开cmd，输入install XML::DOM ，然后测试在rouge的路径下运行rouge1.5.5.pl 和 runRouge-test.pl,分别得到如图结果：
   (https://img-blog.csdn.net/20170505111122201?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDU5NTU4OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
   (https://img-blog.csdn.net/20170505111140295?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDU5NTU4OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
  
  Step2:
配置rouge的环境变量，向PATH中添加一个指向rouge的路径，一个指向rouge\RELEASE-1.5.5，再添加一个指向rouge\RELEASE-1.5.5\data。如果未成功，提供另一种方式，文本文档编辑runROUGE-test.pl，将$ROUGE 变量由../ROUGE-1.5.5.pl修改为ROUGE-1.5.5.pl，这样就可以运行成功了，再次运行会得到如下结果：
(https://img-blog.csdn.net/20170505111626327?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDU5NTU4OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
如果在rouge\release-1.5.5\sample-output看到rouge输出结果信息，这说明rouge配置成功。
 
 Step3:
pyrouge只是方便python调用ROUGE-1.5.5的插件，所以需要告诉pyrouge要调用的文件在哪里。打开你的python，使用pip install pyrouge,安装成功之后，设置pyrouge中ROUGE-1.5.5的路径。使用pyrouge提供的pyrouge_set_rouge_path文件进行安装：
(https://img-blog.csdn.net/20170619215639131?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTWVycnlDYW8=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

输入命令python pyrouge_set_rouge_path The path to store ROUGE-1.5.5 in your computer 

 Step4:
这时基本配置完成了，将自己模型生成的摘要与参考摘要提取出来，使用我们提供的pyrouge_test.py文件进行测评。
