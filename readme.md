# 本程序仅仅是为了能够在12点前上床睡觉，抵制多开程序或者使用多线程等不文明的抢课行为

## 使用说明

把 $$main.py$$ 的第 $23$ 行的账号密码改成自己的账号和密码。第 $$58$$ 行 $$result$$ 后面的数字串格式为“实验代号+第几周+星期几+时间(1代表上午，2代表下午，3代表晚上)”，比如选第7周的1022，时间是周六下午，那么数字串应该是"10220762" 。第 $$59$$ 行 $$eid=basxx$$ 处，将 $$xx$$ 改为所在的周号，比如第7周应该改为 $$eid=bas07$$ 。代码中的例子是选择第15周星期六上午的1022实验。

只有做完上一个实验才能选择下一个实验，经测试，在当前实验做完后，可以选择还没开放的实验。

## 回馈作者

在任何网络社交平台大骂傻逼wwl即可。
