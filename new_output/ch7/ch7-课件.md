--- PAGE 001 ---
# 第七章

## 机械振动

1. 简谐振动
2. 振动的合成与分解
3. 阻尼振动和受迫振动

--- PAGE 002 ---
机械振动——物体在一定位置附近作来回往复的运动。

振动有各种不同的形式：机械振动、电磁振动、...

广义振动：

任一物理量 (如位移、电流等) 在某一数值附近反复变化。

--- PAGE 003 ---
## §7-1 简谐振动

## 🔷 简谐振动

—— 物体振动时, 离开平衡位置的位移 \(x\) (或角位移 \(\theta\) )
随时间 \(t\) 的变化可表示为余弦函数或正弦函数：

\[x = A \cos(\omega t + \varphi)\]

A: 振幅, 振动幅度的大小, 由初条件决定。

\(\omega\) : 角频率 ( 圆频率 ), 振动系统固有的频率

\(\varphi\) : 初相位, 由初条件决定。

--- PAGE 004 ---
物体在平衡位置的两侧，在弹性恢复力和惯性两个因素互相制约下，不断重复相同的运动过程。

## 一、简谐振动方程

1. 动力学特征

系统受力：力的大小与位移成正比，方向与位移方向相反。

\[ F = -k x \]

2. 运动学特征

由牛顿定律： \(m \frac{d^2 x}{dt^2} = -kx\) 得: \(\frac{d^2 x}{dt^2} + \frac{k}{m} x = 0\)

令：

--- PAGE 005 ---
得谐振动的微分方程：

\[ \frac{d^2x}{dt^2} + \omega^2 x = 0 \]

3. 运动方程 --- 微分方程的解 \(x = A \cos{(\omega t + \varphi)}\)

谐振动的运动方程 --- 振动方程。

凡是具有以上受力特征、运动微分方程和运动方程的运动均为简谐振动

\(x \sim t\) 关系曲线称振动曲线。

★ 简谐振动特点：

(1) 等幅振动；

(2) 周期振动。

--- PAGE 006 ---
## 二 描述简谐振动的特征量

谐振动方程：

\(x = A \cos(\omega t + \varphi)\)

1、振幅 \(A\) —— 最大位移的绝对值。

(参考圆的半径)

2、周期、频率和角频率

1）.周期 \(T\) —— 完成一次全振动所需的时间

\(T = \frac{2\pi}{\omega}\)

弹簧振子：\(\omega = \sqrt{\frac{k}{m}}\), ∴ \(T = 2\pi \sqrt{\frac{m}{k}}\)

--- PAGE 007 ---
2). 频率 \(\nu\) ——单位时间内完成全振动的次数。

\[ \nu = \frac{1}{T} = \frac{\omega}{2\pi} \]

3). 角频率 \(\omega\) ——旋转矢量的角速度。(亦称圆频率)

\[ \omega = \frac{2\pi}{T} = 2\pi\nu \]

3、相位和初相

1). 相位 \((\omega t + \phi)\)

决定物体的振动状态或旋转矢量在参考圆上的位置。

(1) \((\omega t + \varphi)\) 可确定 \(t\) 时刻的 \(x\)、\(\nu\)、\(a\) 的大小和方向；

(2) \(\cos(\omega t + \varphi) = \cos[\omega(t + T) + \varphi]\), 突出了振动的周期性。

2). 初相 \(\varphi\) —— \(t=0\) 时刻的相位。

--- PAGE 008 ---
# 4、决定简谐振动各特征量的因素

弹簧振子系统: \(\omega = \sqrt{\frac{k}{m}}\)

\[ T = \frac{2\pi}{\omega} = 2\pi \sqrt{\frac{m}{k}} \]

\[ \nu = \frac{1}{T} = \frac{1}{2\pi} \sqrt{\frac{k}{m}} \]

T—固有周期; ν—固有频率。

::周期和频率是由振动系统决定的。

* 对于一个确定的系统,其频率虽然确定,但其运动状态还要由初条件决定。

* ωt+φ是简谐振动的相位,它决定振动物体在任一时刻的位置和运动状态。

--- PAGE 009 ---
## \(A\) 和 \(\varphi\) 的确定(初始条件)

振动方程： \(x = A \cos(\omega t + \varphi)\)

初始条件：\(t = 0\)，
\[\begin{cases}
x_0 = A \cos \varphi \\
v_0 = -\omega A \sin \varphi
\end{cases}\]
(初位移)
(初速度)

\[ \text{由上式得：} \begin{cases} A = \sqrt{x_0^2 + \frac{v_0^2}{\omega^2}} \\ \tan \varphi = -\frac{v_0}{\omega x_0} \end{cases} \]

★ 注意：

\(\varphi\) 在 \(-\pi \sim \pi\) 之间有两个值, 要由初始条件判断取舍。

--- PAGE 010 ---
## 三、简谐振动的速度、加速度

1. 速度 \(v = \frac{\mathrm{d}x}{\mathrm{d}t} = -\omega A \sin (\omega t + \varphi)\)  \(v_{\text{max}} = \omega A\)

2. 加速度 \(a = \frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}} = -\omega^{2}A \cos (\omega t + \varphi)\)  \(a_{\text{max}} = \omega^{2}A\)

由此看出：速度与位移的相位相差 \(\pi/2\)
加速度与速度的相位相差 \(\pi/2\) ，加速度与位移的相位相差 \(\pi\)

--- PAGE 011 ---
## 第一类问题：由简谐振动运动学方程求未知参数

教材例题 7.1 一质量为 \(0.01\text{kg}\) 的物体做谐振动，振幅为 \(8\text{cm}\)，周期为 4s， \(t=0\) 时，物体位于 \(x=4\text{cm}\) 处并处于 \(x\) 轴正方向运动，求：1) \(t=1\text{s}\) 时，物体的位置坐标、速度和受力；

解：设物体的运动学方程为 \(x = A\sin(\omega t + \phi)\)

当 \(t=1.0\text{s}\) 时，物体的位置坐标、速度和受到的力分别为

\[ x_{t=1.0\text{s}} = 0.08\sin\left(\frac{\pi}{2} + \frac{\pi}{6}\right) = 0.07 \, (\text{m}) \]

\[ \dot{x}_{t=1.0\text{s}} = 0.08 \times \frac{\pi}{2} \cos\left(\frac{\pi}{2} + \frac{\pi}{6}\right) = -0.06 \, (\text{m/s}) \]

\[ f = m \ddot{x}_{t=1.0\text{s}} = -0.01 \times 0.08 \times \left(\frac{\pi}{2}\right)^2 \sin\left(\frac{\pi}{2} + \frac{\pi}{6}\right) = -1.71 \times 10^{-3} \, (\text{N}) \]

## 由此得到运动学方程和速度：

\[ x = 0.08\sin\left(\frac{\pi}{2} t + \frac{\pi}{6}\right) \, \text{m} \]

\[ v = 0.08 \times \frac{\pi}{2} \cos\left( \frac{\pi}{2} t + \frac{\pi}{6} \right) \, \text{m/s} \]

--- PAGE 012 ---
**教材例题 7.1 2)** 若物体在平衡位置并向 \(x\) 轴负方向运动时刻开始计时, 试求初相和由起始位置到 \(x=-8\text{cm}\) 处所需的最短时间.

**解:** 设物体的运动学方向为 \(x = A \sin(\omega t + \phi)\) 当 \(t=0\) 时, \(x=0\), 代入
\[ 0 = 0.08 \sin \phi \quad \text{所以} \quad \phi=0 \text{或} \pi \]

根据 \(t=0\) 时，\(v_0<0\) 这一条件，只能取 \(\phi=\pi\)

运动学方程为 \(x=0.08\sin(\frac{\pi}{2}t+\pi)\) m

**可见，同一振动不同起始计时时刻，有不同的初相位。**
设起始 \(x=0\) 到 \(x=-8\text{cm}\) 所需的最短时间为 \(t'\)，则

\[ -0.08 = 0.08 \sin\left(\frac{\pi}{2}t' + \pi\right) \]

\[ \left(\frac{\pi}{2}t' + \pi\right) = \arcsin(-1) = \frac{3\pi}{2} \]

\(t' = 1\text{s}\)

--- PAGE 013 ---
**教材例题 7.3** 如图所示为一谐振动的位移 - 时间曲线，求振动方程。

**解：**该物体的运动学方程为 \(x = A \cos(\omega t + \phi)\)

由图知 \(A=6 \, \text{cm}, t=0\) 时 \(x_0=-3 \, \text{cm}\)

代入运动学方程 \(x_0=-3=6\cos\varphi\)

\[ \varphi = \frac{2}{3}\pi \text{或} \frac{4}{3}\pi, \text{由 } v_0 > 0 \text{只能取 } \frac{4}{3}\pi \]

再由图知 \(t=1.5\) 时，\(x=3\) cm, 再代入运动学方程

\[ 
\begin{align*} 
3 &= 6\cos\varphi' = 6\cos(\omega \times 1.5 + \frac{4}{3}\pi) \\ 
\varphi' &= \frac{\pi}{3} \quad \text{或} \quad \frac{5\pi}{3} 
\end{align*} 
\]

\[ \omega \times 1.5 + \frac{4}{3} \pi = \frac{5\pi}{3} \quad \omega = \frac{2\pi}{9} \]

**振动方程为**

\[ x = 6\cos\left(\frac{2\pi}{9}t - \frac{4\pi}{3}\right) \, \text{cm} \]

--- PAGE 014 ---
## 第二类问题：证明系统是简谐振动和求系统固有振动频率（本章重点）

1. 确定研究对象，建立坐标系，受力或力矩分析；

2. 由牛二定律或转动定律写出动力学基本方程；

3. 将动力学基本方程化为二阶常微分方程，将其与标准振动微分方程做比较，判定是否为简谐振动；

4. 由振动微分方程的常系数项写出振动角频率或周期；

5. 由t=0时的初始条件 x(0)和v(0)确定振幅和初相；

6. 比较简谐振动运动学方程的标准形式写出运动学方程。

--- PAGE 015 ---
例题1 一轻弹簧竖直悬挂，下端重物质量 \(m=0.1\text{kg}\) ，平衡时弹簧伸长 \(l=9.8 \times 10^{-2}\text{m}\) 。今使物体在平衡位置获得向下的初速度 \(v_0=1\text{m}.\text{s}^{-1}\) ，则物体将在竖直方向运动。

求：(1) 运动方程；(2) 最大回复力。

解：(1) 选平衡位置为坐标原点如图。

\[
\begin{align*}
\text{平衡时 } m g = k l, & \quad \therefore k = \frac{mg}{l} \\
\text{位移为 } x &\text{ 时 } F = mg - k(l + x) = -kx \\
&\quad \therefore m \frac{d^2 x}{dt^2} = -kx, \quad \frac{d^2 x}{dt^2} + \frac{k}{m}x = 0 \\
&\quad \text{所以物体做谐振动，且有：} \omega = \sqrt{\frac{k}{m}}
\end{align*}
\]

--- PAGE 016 ---
已知得：\(\omega = \sqrt{\frac{k}{m}} = \sqrt{\frac{mg/l}{m}} = \sqrt{\frac{g}{l}} = \sqrt{\frac{10}{0.1}} = 10 \, (\text{s}^{-1})\)

由初始条件得：

\[ 
\begin{cases} 
A = \sqrt{x_0^2 + \frac{v_0^2}{\omega^2}} = \sqrt{0 + \frac{1^2}{10^2}} = 0.1 \text{ (m)} \\ 
\tan \varphi = - \frac{v_0}{\omega x_0} = -\frac{1}{10 \times 0} = -\infty, \quad \varphi = -\frac{\pi}{2} 
\end{cases} 
\]

振动方程为：\(x = 0.1 \cos(10t - \frac{\pi}{2})\) (SI)

(2) 最大回复力：\(F_{\text{max}} = k x_{\text{max}} = k A = 1\) (N)

重力只影响谐振子系统的平衡位置；这样的结论对所有作用于谐振子系统的恒力都成立！

--- PAGE 017 ---
## 例题2 证明单摆的运动是谐振动 \((\theta < 5^\circ)\)

系统受力矩: 
\[ M = -mgl \sin \theta \approx -mgl\theta \]

由转动定律: 
\[ M = J \frac{d^2\theta}{dt^2} = -mgl\theta \]

\[ m l^2 \frac{d^2\theta}{dt^2} = -mgl\theta, \quad \frac{d^2\theta}{dt^2} + \frac{g}{l} \theta = 0 \]

令 \(\omega = \sqrt{\frac{g}{l}}\) 得: \(\frac{d^2\theta}{dt^2} + \omega^2\theta = 0\)

单摆的运动是谐振动。周期 \(T = 2\pi \sqrt{\frac{l}{g}}\)

振动方程: \( \theta = \theta_0 \cos(\omega t + \varphi) \)

--- PAGE 018 ---
振动方程：\(\theta = \theta_0 \cos(\omega t + \varphi)\)

★ 注意：初相 \(\varphi\) 与角位移 \(\theta\) 的区别！

★ 说明：

(1) 单摆周期 \(T\) 与摆锤的质量 \(m\) 无关。

(2) 由 \(T, l\) 可测量该地的重力加速度

(3) 单摆在小角度近似下为谐振动。

(4) \(\theta\) 较大时：

\[
\begin{align*}
M &= -mgl \sin \theta = -mgl(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots) \\
T &= 2\pi \sqrt{\frac{l}{g}}\left( 1 + \frac{1}{2^2}\sin^2 \frac{\theta}{2} + \frac{1}{2^2} \cdot \frac{3^2}{4^2}\sin^4 \frac{\theta}{2} + \dots \right)
\end{align*}
\]

--- PAGE 019 ---
(3) 复摆

一任意形状的刚体，支在过 O 点的光滑水平轴上，使刚体偏离平衡位置后释放，刚体就在平衡位置附近来回摆动，这样的摆叫复摆（也叫物理摆），如图所示。刚体质量为 m，质心为 c，质心至转轴的距离为 l，且知刚体对该轴的转动惯量为 J

--- PAGE 020 ---
系统受力矩：\(M = -mgl\sin\theta\)

\[ \theta \text{ 很小时} \quad M = J\frac{d^2\theta}{dt^2} = -mgl\theta \]

\[ \frac{d^2\theta}{dt^2} + \frac{mgl}{J}\theta = 0, \quad \frac{d^2\theta}{dt^2} + \omega^2\theta = 0 \]

振动方程：\(\theta = \theta_0 \cos(\omega t + \phi)\)

角频率：\(\omega = \sqrt{\frac{mgl}{J}}\)  周期：\(T = 2\pi \sqrt{\frac{J}{mgl}}\)

* 说明：(1) 小角度近似下为谐振动。
  (2) 可测量物体对转轴的转动惯量 \(J\)。

--- PAGE 021 ---
例3 劲度系数为 \(k\) 的轻弹簧一端固定在墙上，另一端连接一质量为 \(m\) 的物体，跨过一质量为 \(M\) 、半径为 \(R\) 的定滑轮，平衡时弹簧伸长 \(l\) （如图）。求：该系统的振动圆频率。

解：在平衡位置处： \(mg = kl\) 以平衡位置为坐标原点，向下为正建立 \(x\) 坐标。

\(m\) 运动到 \(x\) 处时，分析

--- PAGE 022 ---
\[\begin{aligned}
mg - T_1 &= ma = m \frac{d^2x}{dt^2} \\
(T_1 - T_2)R &= \frac{1}{2}MR^2 \alpha \\
T_2 &= k(x+l) \\
\alpha &= \frac{a}{R} = \frac{1}{R} \frac{d^2x}{dt^2}
\end{aligned}\]

解上面的方程组得：

\[ \frac{d^2x}{dt^2} + \frac{k}{m + \frac{M}{2}} x = 0 \]

系统的振动圆频率：

\[ \omega = \sqrt{\frac{k}{m + \frac{M}{2}}} \]

--- PAGE 023 ---
**7-1** 如图7-1所示，一直角均质细杆，水平部分杆长为 \(l\) ，质量为 \(m\) ，竖直部分杆长为2l，质量为2m，细杆可绕直角顶点处的固定轴O 无摩擦地转动，水平杆的未端与劲度系数为 \(k\) 的弹簧相连，平衡时水平杆处于水平位置，试求杆作微小摆动时的周期。

解 设平衡时弹簧伸长\(x_0\)，则根据细杆系统关于 O 点的合外力矩为零，有

\[k x_0 l = mg \frac{l}{2} \qquad (1)\]

当杆摆到任意角度 \(\theta\) 位置时，弹簧的伸长量为 \((x_0 + x)\)，细杆系统所受的合外力矩为

\[M = mg \frac{l}{2} \cos \theta - 2mg l \sin \theta - k (x_0 + x) l \cos \theta \quad (2)\]

因为摆动幅度非常微小，因而有

\[\begin{aligned} x &\approx l \theta \\ \cos \theta &\approx 1 \\ \sin \theta &\approx \theta \end{aligned}\]

将以上各式及式(1)代入到式(2)中，有
\[M = -(2mgl + kl^2) \theta\]

--- PAGE 024 ---
根据刚体定轴转动定律,有
\[ J \frac{d^2 \theta}{dt^2} = - (2mgl + kl^2) \theta \]

即
\[ \frac{d^2 \theta}{dt^2} + \frac{2mgl + kl^2}{J} \theta = 0 \]

式中 \(J\) 为细杆关于转轴 O 的转动惯量, 为

\[ J = \frac{1}{3} ml^2 + \frac{1}{3} (2m)(2l)^2 = 3ml^2 \]

代入上式后,有
\[ \frac{d^2 \theta}{dt^2} + \frac{2mg + kl}{3ml} \theta = 0 \]

因而,细杆绕 O 轴的微小摆动是简谐振动,

其角频率为 \( \omega = \sqrt{\frac{2mg + kl}{3ml}} \)

周期为 \( T = 2\pi \sqrt{\frac{3ml}{2mg + kl}} \)

--- PAGE 025 ---
## 四、简谐振动的旋转矢量表示法（矢量图解法）

作坐标轴Ox，自原点作一矢量 \(\vec{A}\)，其大小为A，
以角速度ω绕O点逆时针旋转。

\(\vec{A}\) — 旋转矢量

初始时与x轴夹角为φ，

t时刻与x轴夹角为ω t+φ

其矢端M在x轴投影
P点的位移：

\[x = A \cos (\omega t + \phi)\]

P点的运动规律—简谐振动。

--- PAGE 026 ---
例 7.7 设一音叉的振动为谐振动,其角频率 \(\omega=6.28\times10^{2} \mathrm{rad} / \mathrm{s}\), 音叉尖端的振幅 \(A\) 为 \(1.0 \mathrm{mm}\). 试用旋转矢量法求以下两种情况的初相, 并写出运动学方程. (1)当 \(t=0\) 时, 音叉尖端通过平衡位置并向 \(x\) 轴负方向运动; (2)当 \(t=0\) 时, 音叉尖端在 \(x\) 轴的负方向一边, 离开平衡位置距离为振幅之半, 且向 \(x\) 轴负方向运动.

解 (1) 根据题设, \(t=0\) 时, 旋转矢量的位置, 如图 7.12(a) 所示, 从而得

\[ \varphi = \frac{1}{2}\pi \]

\(x=0.1\cos\left(6.28\times10^2 t+\frac{1}{2}\pi\right) \mathrm{cm}\)

(2) 根据题设, \(t=0\) 时, 旋转矢量的位置,
如图7.12(b)所示, 从而得 \(\varphi=\frac{2}{3}\pi\), 故运动学

\[ x = 0.1 \cos \left( 6.28 \times 10^{2} t + \frac{2}{3} \pi \right) \text{ cm} \]

--- PAGE 027 ---
## 五、简谐振动的能量

1. 动能

\[E_k = \frac{1}{2} mv^2 = \frac{1}{2} m\omega^2 A^2 \sin^2(\omega t + \varphi)\]

\[E_k = \frac{1}{2} kA^2 \sin^2(\omega t + \varphi)\]

2. 势能

\[E_P = \frac{1}{2} kx^2 = \frac{1}{2} kA^2 \cos^2(\omega t + \varphi)\]

3. 总能

\[E = E_k + E_p = \frac{1}{2} kA^2\]

* 结论：简谐振动的总能量与振幅的平方成正比且守恒。

--- PAGE 028 ---
\[
E = \frac{1}{2} kA^2
\]

\[
\begin{align*}
& E_k = \frac{1}{2} kA^2 \cos^2 \omega t \\
& E_p = \frac{1}{2} kA^2 \sin^2 \omega t
\end{align*}
\]

★ 说明：

(1) 在运动过程中，动能和势能相互转换。

(2) 总机械能保持不变, 且与振幅的平方成正比。

(3) 动能和势能的极大值相等。

--- PAGE 029 ---
4. 能量平均值

\[\bar{E}_k = \frac{1}{T} \int_{0}^{T} \frac{1}{2} m \omega^2 A^2 \sin^2(\omega t + \varphi) dt = \frac{1}{4} kA^2\]

\[\bar{E}_p = \frac{1}{T} \int_{0}^{T} \frac{1}{2} mkA^2 \cos^2(\omega t + \varphi) dt = \frac{2}{4} kA^2\]

\[\therefore \quad \bar{E}_k = \bar{E}_p = \frac{1}{2} E\]

★ 结论：简谐振动的重要特征：

简谐振动系统的动能和势能在一个周期内的平均值相等，且等于总能量的一半。

--- PAGE 030 ---
**例 7.9** 图7.15所示为截面积为 \(S\) 的U形管，内装有密度为 \(\rho\)、长度为 \(l\) 的液体柱，受到扰动后管内液体发生振荡，试写出液体柱的运动微分方程.不计各种阻力。

在液体平衡时的液面上,取一点 \(O\) 为 \(x\) 轴的原点, \(x\) 轴向上为正,以液体为研究对象,时刻 \(t\) ,液体的动能 \(E_k\) 为
\(E_k=\frac{1}{2}Sl\rho x^{2}\)

要计算重力势能 \(E_p\),只需计算 \(x\) 小段液柱从左边移到右边所需做的功 \(A\) (为什么?),因此有

\[E_p = A = \rho S x^2 g\]

根据机械能守恒定律,有

\[E = E_k + E_p = \frac{1}{2}Sl\rho x^2 + \rho S x^2 g = \text{常量}\]

将上式对 \(t\) 求导,经整理后,有

\[\dot{x} + \left(\frac{2g}{l}\right)x = 0\]

液柱的运动为谐振动,其振动的周期 \(T\) 为

\[T = 2\pi \sqrt{\frac{l}{2g}}\]

--- PAGE 031 ---
## §7 - 2 简谐振动的合成

## 一、同振向、同频率谐振动的合成

\[x_1 = A_1 \cos(\omega t + \varphi_1), \quad x_2 = A_2 \cos(\omega t + \varphi_2)\]

### 1. 数学分析法

\[
\begin{align*}
x &= x_1 + x_2 = A_1 \cos(\omega t + \varphi_1) + A_2 \cos(\omega t + \varphi_2) \\
&= (A_1 \cos \varphi_1 + A_2 \cos \varphi_2) \cos \omega t \\
&\quad - (A_1 \sin \varphi_1 + A_2 \sin \varphi_2) \sin \omega t
\end{align*}
\]

令 \(\begin{cases} A \cos \varphi = A_1 \cos \varphi_1 + A_2 \cos \varphi_2 \\ A \sin \varphi = A_1 \sin \varphi_1 + A_2 \sin \varphi_2 \end{cases}\)

则上式得

\[x = A \cos \varphi \cos \omega t - A \sin \varphi \sin \omega t = A \cos (\omega t + \varphi)\]

--- PAGE 032 ---
\[x = A \cos\left(\omega t + \varphi\right) \quad (7-16)\]

## 结论：

(1) 同振向同频率谐振动的合成仍为谐振动。

(2) 合振动的频率与两分振动的频率相同。

(3) 合振动振幅和初相由下式决定：

\[ ①^{2} + ②^{2} \quad A = \sqrt{A_{1}^{2} + A_{2}^{2}} + 2A_{1}A_{2}\cos(\varphi_{2} - \varphi_{1}) \quad (7-17) \\ \text{②} \quad ① \quad \varphi = \arctan \frac{A_{1}\sin\varphi_{1} + A_{2}\sin\varphi_{2}}{A_{1}\cos\varphi_{1} + A_{2}\cos\varphi_{2}} \quad (7-18) \]

--- PAGE 033 ---
## 2. 旋转矢量法

\[ \vec{A} = \vec{A}_1 + \vec{A}_2 \]

\[ t = 0 \] 时刻的矢量图

\[ \begin{aligned} A &= \sqrt{A_1^2 + A_2^2 + 2A_1A_2 \cos(\varphi_2 - \varphi_1)} \\ \varphi &= \arctan \frac{A_1 \sin \varphi_1 + A_2 \sin \varphi_2}{A_1 \cos \varphi_1 + A_2 \cos \varphi_2} \end{aligned} \]

## 3. 相位差

\[ \begin{aligned} x_1 &= A_1 \cos(\omega t + \varphi_1), & x_2 &= A_2 \cos(\omega t + \varphi_2) \\ \Delta \varphi &= (\omega t + \varphi_2) - (\omega t + \varphi_1) = \varphi_2 - \varphi_1 \end{aligned} \]

两同频率谐振动的相位差：\(\Delta \varphi = (\varphi_2 - \varphi_1)\) （初相差）

--- PAGE 034 ---
4. 同相和反相

\[(1) \text{ 同相: } \Delta \varphi = \varphi_2 - \varphi_1 = 2k\pi\]

\[(k = 0, \pm1, \pm2, \cdots)\]

\(\Rightarrow A = A_1 + A_2 \quad \text{合振幅最大}\)

两振动步调相同，振动加强，同相。

\[(2) \text{ 反相: } \Delta \varphi = \varphi_2 - \varphi_1 = (2k + 1)\pi\]

\[(k = 0, \pm 1, \pm 2, \cdots)\]

\(\Rightarrow A = A_1 - A_2 \quad \text{合振幅最小}\)

两振动步调相反，振动减弱，反相。

当 \(A_1 = A_2\) 时，静止。

--- PAGE 035 ---
### 5. 超前和落后

若 \(\Delta \varphi = \varphi_2 - \varphi_1 > 0\)

则称：\(x_2\) 比 \(x_1\) 超前；

或 \(x_1\) 比 \(x_2\) 落后。

超前/落后以

\(\Delta \varphi < \pi\)

的相位角来判断。

x₂ 比 x₁ 超前

### 6. 多个同振向、同频率谐振动的合成

\[\vec{A} = \vec{A}_1 + \vec{A}_2 + \vec{A}_3 + \dots\]

采用旋转矢量法：

各分振动矢量首尾依次相接。

--- PAGE 036 ---
## 二、同振向、不同频率谐振动的合成一拍

\[
\begin{align*}
x_1 &= A_1 \cos(\omega_1 t + \varphi_1), \quad x_2 = A_2 \cos(\omega_2 t + \varphi_2) \\
\Delta \varphi &= (\omega_2 t + \varphi_2) - (\omega_1 t + \varphi_1) \\
&= (\omega_2 - \omega_1) t + (\varphi_2 - \varphi_1)
\end{align*}
\]

★ 相位差随时间变化；合振动不再是简谐振动。

为使讨论简便，设两振动的 \(A_1 = A_2\), \(\varphi_1 = \varphi_2 = 0\)。

\(则有 : \begin{cases} x_1 = A \cos \omega_1 t = A \cos 2\pi v_1 t \\ x_2 = A \cos \omega_2 t = A \cos 2\pi v_2 t \end{cases} \)

合振动方程为：

\[x = x_1 + x_2 = A \cos 2\pi v_1 t + A \cos 2\pi v_2 t\]

--- PAGE 037 ---
\[
\begin{align*}
x = 2A \cos(2\pi \frac{V_2 - V_1}{2}t) \cos(2\pi \frac{V_2 + V_1}{2}t) \\
= A' \cos(2\pi V t + \varphi)
\end{align*}
\]

合振动频率： \(v = \frac{V_2 + V_1}{2}\)

\[
\text{合振动振幅} : A' = 2A \cos 2\pi \frac{V_2 - V_1}{2} t
\]

★ 讨论：两频率都较大，而频率差很小的情况
合振幅出现时大时小的现象——拍现象。

--- PAGE 038 ---
* 拍频 – 单位时间内合振幅极大出现的次数。

\[ V_{\text{拍}} = |V_2 - V_1| \quad (7-25) \]

振幅变化的周期为： \(T_{\text{拍}} = \frac{1}{\sqrt{|V_2 - V_1|}}\)

--- PAGE 039 ---
拍现象的应用：

- 用音叉振动校准乐器

- 测定超声波

- 测定无线电频率

- 调制高频振荡的振幅和频率等

三、同振向倍频谐振动的合成

\[v_1 = 5 s^{-1}; v_2 = 15 s^{-1}; v = 5 s^{-1}\]

--- PAGE 040 ---
# 三 相互垂直振向简谐振动的合成

## 一、相互垂直的同频率谐振动的合成

\[x = A \cos(\omega t + \alpha)\]

\[y = B \cos(\omega t + \beta)\]

消去参数 \(t\), 得轨迹方程:

\[\frac{x^2}{A^2} + \frac{y^2}{B^2} -\frac{2xy}{A B} \cos(\beta - \alpha) = \sin^2(\beta - \alpha) \qquad (7-31)\]

是一个椭圆类二次曲线方程。

--- PAGE 041 ---
## 讨论：

1. \(\beta - \alpha = 0\) (两个分振动同相)

轨迹：\(y=\frac{B}{A}x\)

运动方程：\(S = \sqrt{A^2 + B^2 \cos(\omega t + \varphi)}\)

是谐振动，角频率与初相不变。

2. \(\beta - \alpha = \pi\) (两个分振动反相)

轨迹：\(y = -\frac{B}{A}x\)

运动方程：\(S = \sqrt{A^2 + B^2 \cos(\omega t + \varphi)}\)

是谐振动，角频率与初相不变。

(1) 对称振动。

--- PAGE 042 ---
3. \(\beta - \alpha = \frac{\pi}{2}\)

轨迹： \(x^2 + \frac{y^2}{A^2B^2} = 1\)

是椭圆运动，方向时顺时针（右旋）。

4. \(\beta - \alpha = \frac{3\pi}{2}\)
\((y\)比\(x\)相位落后\(\pi/2\))

轨迹： \(\frac{x^2}{A^2} + \frac{y^2}{B^2} = 1\)

是椭圆运动，方向时逆时针（左旋）。
\(A=B\) 时，为圆轨道，即作圆周运动。

3. \(\beta - \alpha = \frac{\pi}{2}\)

\((y\) 比 \(x\) 相位落后 \(\pi/2\)

轨迹： \(\frac{x^2}{A^2} - \frac{y^2}{B^2} = 1\)

--- PAGE 043 ---
\[
\frac{x^2}{A^2} + \frac{y^2}{B^2} - \frac{2xy}{AB} \cos(\beta - \alpha) = \sin^2(\beta - \alpha)
\]

图 7—

--- PAGE 044 ---
## 二、垂直方向不同频率简谐振动的合成

### 1. 两分振动频率相差很小

\[ \Delta \varphi = (\omega_2 - \omega_1)t + (\varphi_2 - \varphi_1) \]

可看作两频率相等而 \(\varphi_2 - \varphi_1\) 随 t 缓慢变化，
合运动轨迹将按图依次循环地缓慢变化。

--- PAGE 045 ---
2. 两振动的频率相差很大

合振动轨道一般不是封闭曲线,但当频率有简单整数比
关系时,是稳定的封闭曲线,称为"李萨如图形"。

\[T_x : T_y = 1 : 2\]

\[T_x : T_y = 2 : 3\]

\[T_x : T_y = 3 : 4\]

★测量谐运动的频率和相互垂直的两个简谐振动的相位差。

--- PAGE 046 ---
## §7 - 3 阻尼振动 受迫振动 共振

### 一、阻尼振动

阻尼振动 — 振幅（或能量）随时间减小的振动。

阻尼振动

摩擦阻尼：系统受到摩擦力的作用，克服阻力作功，系统的振动能量转化为热能。

辐射阻尼：振动以波的形式向外传播，使振动能量向周围辐射出去。

--- PAGE 047 ---
## 1. 阻尼振动运动微分方程

有粘滞阻力时弹簧振子:

阻力: \(f_r = -\gamma v = -\gamma \frac{dx}{dt}\)

动力学方程: \(\frac{m \frac{d^2 x}{dt^2}}{m} = -kx - \gamma \frac{dx}{dt}\) (7-36)

运动微分方程: \(\frac{d^2 x}{dt^2} + 2\beta \frac{dx}{dt} + \omega_0^2 x = 0\) (7-37)

其中:

\(\omega_0 = \sqrt{\frac{k}{m}},\) 称固有角频率, 由系统本身性质决定;

\(\beta = \gamma \sqrt{2m},\) 称阻尼因子, 由阻力系数 \(\gamma\) 决定。

--- PAGE 048 ---
## 2. 弱阻尼 (\( \beta < \omega_0 \))

方程 (7-37) 的解为：\(x = A_0 e^{-\beta t} \cos(\omega t + \varphi)\) (7-38)

其中：\(\omega = \sqrt{\omega_0^2 - \beta^2}\) —— 阻尼振动角频率 (7-39)

\[T = \frac{2\pi}{\omega} = \frac{2\pi}{\sqrt{\omega_0^2 - \beta^2}} \qquad \text{—— 阻尼振动周期} \quad (7-40)\]

弱阻尼曲线：

- 振幅随时间 \(t\) 作指数衰减；

- 近似为简谐振动；
- 阻尼振动周期比系统的固有周期长。

--- PAGE 049 ---
## 3. 临界阻尼和过阻尼

\[ \beta < \omega_0 : \text{弱阻尼}; \]

\[ \beta = \omega_0 : \text{临界阻尼}; \]

临界阻尼是物体不作往复运动的极限，从周期振动变为非周期振动。

\[ \beta > \omega_0 : \text{过阻尼}; \]

振动从开始最大位移缓慢回到平衡位置，不再做往复运动，非周期运动。

--- PAGE 050 ---
## 二、受迫振动

—— 系统在周期性外力持续作用下所发生的振动。

弹性力: \(-k x\), 阻尼力: \(-γ v\), 驱动力: \(H \cos{\omega t}\)

受迫振动的运动微分方程:

\[
\begin{align*}
m \frac{d^2 x}{dt^2} &= -kx - γ \frac{dx}{dt} + H \cos{\omega t} \\
\frac{d^2 x}{dt^2} + 2β \frac{dx}{dt} + \omega_0^2 x &= h \cos{\omega t} \tag{7-41}
\end{align*}
\]

微分方程的解为

\[
x = A_0 e^{-\beta t} \cos \left( \omega_0^2 - \beta^2 t + \varphi_0 \right) + A \cos \left( \omega t + \varphi \right) \tag{7-42}
\]

--- PAGE 051 ---
\[
\begin{align*}
\dot{x} &= A_0 e^{-\beta t} \cos\left(\omega_0^2 - \beta^2 t + \varphi_0\right) + A \cos\left(\omega t + \varphi\right) \\
&\quad \quad \quad \uparrow\\
\text{阻尼振动} &\quad \space\space压缩力
\end{align*}
\]

经一段时间受迫振动 —— 简谐振动：

\[
x = A \cos(\omega t + \varphi)
\]

其振幅为：

\[
A = \frac{h}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2}}
\qquad (7-47)
\]

--- PAGE 052 ---
## 三、共振

一驱动力的角频率为某定值时受迫振动的振幅达到极大值的现象。

由 (7-47) 式

\[
A = \frac{h}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2}}
\]

令：

\[
\frac{dA}{d\omega} = \frac{d}{d\omega} \left( \frac{h}{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^3} \right) = 0
\]

得：

共振角频率： \(\omega_{\text{共}} = \sqrt{\omega_0^2 - 2\beta^2}\) (7-48)

共振振幅： \(A_{\text{共}} = \frac{h}{2\beta\sqrt{\omega_0^2 - \beta^2}}\) (7-49)

--- PAGE 053 ---
\[
\omega_{\theta} = \sqrt{\omega_{0}^{2} - 2\beta^{2}}, \quad A_{\theta} = \frac{h}{2\beta\sqrt{\omega_{0}^{2} - \beta^{2}}}
\]

★分析：

(1) \(\beta\) 越小时, \(\omega_{\text{共}}\) 越接近于 \(\omega_0\) ,

\(A_{\text{共}}\) 越大。

(2) \(\beta = 0\) 时, \(\omega_{\theta} = \omega_0\) ,

\(A_{\theta} \to \infty\) 尖锐振动。

★强迫力的方向永远与物体运动方向相同。

--- PAGE 054 ---
## ✶应用：

(1) 电磁共振选台（收音机）；
(2) 乐器利用共振提高音响效果；
(3) 研究避免共振的破坏的措施等。

❖ 破坏外力（强迫力）的周期性

❖ 改变系统固有频率

❖ 改变外力的频率

❖ 增大系统阻尼力

❇ 改变系统固有频率
❇ 改变外力的频率
❇ 增大系统阻尼力

塔科马海峡大桥的共振断蹍

❸ 受迫振动与简谐振动有何不同？
