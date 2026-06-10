--- PAGE 001 ---
# 第8章 机械波 

8.1 机械波的产生和传播 

8.2 平面简谐波 

8.3 波的能量 

8.4 惠更斯原理 

8.5 波的干涉 

8.6 驻波 

8.7 多普勒效应

--- PAGE 002 ---
## § 8.1 机械波的产生和传播 

### 一. 机械波的产生 

机械波：机械振动以一定速度在弹性介质中由近及远地传播出去，就形成机械波。 

条件 {
    波源：作机械振动的物体
    弹性介质：承担传播振动的物质 

### 二. 横波和纵波 

横波：介质质点的振动方向与波传播方向相互垂直的波；如柔绳上传播的波。 

纵波：介质质点的振动方向和波传播方向相互平行的波；如空气中传播的声波。

--- PAGE 003 ---
波动是物质的振动状态和能量在时空中传播和分布的一种普遍形式。

--- PAGE 004 ---
## 结论 

(1) 波动中各质点并不随波前进; 

(2) 各个质点的相位依次落后，波动是相位的传播； 

(3) 波动曲线与振动曲线不同。

--- PAGE 005 ---
## 三. 波面和波线 

波面 在波传播过程中，任一时刻媒质中振动相位相同的点联结成的面。 

波纹 沿波的传播方向作的有方向的线。 

波前 在某一时刻，波传播到的最前面的波面。 

<center>球面波</center> 

<center>柱面波</center> 

注意 在各向同性均匀媒质中，波线上波面。

--- PAGE 006 ---
# 四. 波长 周期 频率和波速 

波长 (λ): 同一波线上相邻两个相位差为 2π 的质点之间的距离; 即波源作一次完全振动, 波前进的距离。
波长反映了波的空间周期性。 

周期(T): 波前进一个波长距离所需的时间。周期表征了波的时间周期性。 

频率(ν): 单位时间内, 波前进距离中完整波的数目。频率与周期的关系为 \(ν = \frac{1}{T}\) 

波速(u): 振动状态在媒质中的传播速度。波速与波长、周期和频率的关系为 \(u = \frac{\lambda}{T} = vλ\)

--- PAGE 007 ---
说明 

(1) 波的周期和频率与媒质的性质无关；一般情况下，与波源振动的周期和频率相同。 

(2) 波速实质上是相位传播的速度，故称为相速度；其大小主要决定于媒质的性质，与波的频率无关。 

例如： 

a. 拉紧的绳子或弦线中横波的波速为： 

\[u_t = \frac{T}{\mu} \quad \{ \begin{array}{l} T \text{ — 张力} \\ \mu \text{ — 线密度} \end{array} \]

b. 均匀细棒中，纵波的波速为： 

\[u_l = \frac{Y}{\rho} \quad \{ \begin{array}{l} Y \text{ — 固体棒的杨氏模量} \\ \rho \text{— 固体棒的密度} \end{array} \]

--- PAGE 008 ---
8.2 平面简谐波

--- PAGE 009 ---
# 一. 平面简谐波的波函数 

一般波函数 \(y = f(x,t)\)

简谐振动 \(y = A\cos(\omega t + \varphi)\)

简谐振动——>平面简谐波的波函数

若 \(y_o = A\cos(\omega t + \varphi_o)\) 

从时间看，\(P\) 点 \(t\) 时刻的位移是 \(O\) 点 \(t - \frac{x}{u}\) 时刻的位移； 

从相位看，\(P\) 点处质点振动相位较 \(O\) 点处质点相位落后 \(\omega \frac{x}{u}\) 

\[y_p(x,t) = A\cos[\omega(t - \frac{x}{u}) + \varphi_0]\]

\(P\) 为任意点 \(y(x,t) = A\cos[\omega(t - \frac{x}{u}) + \varphi_1]\) (波函数)

--- PAGE 010 ---
波函数的
其它形式 

\[
\begin{align*}
y(x, t) &= A \cos[2\pi(t \nu - \frac{x}{l}) + \varphi_0] \\
y(x, t) &= A \cos[2\pi(\frac{t}{T} - \frac{x}{\lambda}) + \varphi_0] \\
y(x, t) &= A\cos[\frac{2\pi}{\lambda}(ut-x)+\varphi_0]
\end{align*}
\]

讨论 

(1) 由波函数可知波的传播过程中任意两质点 \(x_1\) 和 \(x_2\) 振动的相位差为 

\[
\Delta = [\omega(t - \frac{x_2}{u}) + \varphi_0] - [\omega(t - \frac{x_1}{u}) + \varphi_0] = \frac{\omega}{u}(x_1 - x_2)
\]

\(x_2>x_1\), \(\Delta<0\), 说明 \(x_2\) 处质点振动的相位总落后于 \(x_1\) 处质点的振动;

--- PAGE 011 ---
(2) u 实际上是振动相位的传播速度。 

\(t_1\) 时刻\(x_1\)处的振动状态经\(\Delta t\)时间传播到\(x_1+\Delta x\)处,则 

\[ \omega(t_1 - \frac{x_1}{u}) = \omega(t_1 + \Delta t - \frac{x_1 + \Delta x}{u}) \]

可得到 

\[ u = \frac{\Delta x}{\Delta t} \]

(3) 若波沿轴负向传播时,同样可得到波函数: 

\[ y(x,t) = A\cos[\omega(t + \frac{x}{u}) + \varphi_0] \]

\[ y(x,t] = A\cos[2\pi(yt + \frac{x}{\lambda}) + \varphi_0] \]

\[ y(x,t) | = A \cos[2\pi(\frac{t}{T} + \frac{x}{\lambda}) + \varphi_0] \]

\[ y(x,t) | = A \cos[\frac{2\pi}{\lambda}(ut + x) + \varphi_0] \]

--- PAGE 012 ---
## 二. 波函数的物理意义 

(1) 振动状态的空间周期性 

\(y(x + \lambda , t) = y(x, t)\)，说明波线上振动状态的空间周期性 

(2) 波形传播的时间周期性 

\(y(x, t + T) = y(x, t)\)，说明波形传播的时间周期性 

(3) \(x\) 给定，\(y = y(t)\) 是 \(x\) 处振动方程 

(4) \(t\) 给定，\(y = y(x)\) 表示 \(t\) 时刻的波形图 

(5) \(y\) 给定, \(x\) 和 \(t\) 都 

在变化，表明波形传播和分布的
时空周期性。

--- PAGE 013 ---
例 一平面简谐波沿x轴正方向传播，已知其波函数为 

\[y = 0.04 \cos \pi (50t - 0.10x) \text{ m}\]

求 (1) 波的振幅、波长、周期及波速; 

(2) 质点振动的最大速度。 

解 (1) a. 比较法(与标准形式比较) 

\[ \text{标准形式} \quad y(x,t) = A \cos[2\pi(t - \frac{x}{\lambda}) + \varphi_0] \]

\[ \text{波函数为} \quad y = 0.04 \cos 2 \pi \left( \frac{50}{2} t - \frac{0.10}{2} x \right) \]

\[ \text{比较可得} \quad A = 0.04 \text{ m} \quad T = \frac{2}{50} = 0.04 \text{ s} \]

\[ \lambda = \frac{2}{0.10} = 20 \text{ m} \quad u = \frac{\lambda}{T} = 500 \text{ m/s} \]

--- PAGE 014 ---
b. 分析法 (由各量物理意义, 分析相位关系) 

振幅 

\[A = y_{\max} = 0.04 \text{ m}\]

波长 

\[\pi(50t - 0.10x_1) - \pi(50t - 0.10x_2) = 2\pi \\
\lambda = x_2 - x_1 = 20 \text{ m}\]

周期 

\[\pi(50t_2 - 0.10x) - \pi(50t_1 - 0.10x) = 2\pi\]

\[T = t_2 - t_1 = 0.04 \text{ s}\]

波速 

\[\pi(50t_2 - 0.10x_2) = \pi(50t_1 - 0.10x_1)\]

\[u = \frac{x_2 - x_1}{t_2 - t_1} = 500 \text{ m/s}\]

\[v = \frac{\partial y}{\partial t} = -0.04 \times 50\pi \sin\pi (50t - 0.10x)\]

\[v_{\max} = 0.04 \times 50\pi = 6.28 \text{ m/s} \neq u\]

--- PAGE 015 ---
例2: 一平面简谐波沿x轴正向传播, 已知 A=1.0 m, T=2.0 s, λ=4.0 m. t=0时坐标原点处质点位于平衡位置沿y轴正向运动。求: (1) 波动方程; (2): t=1.0 s 时波形方程并画出波形图; (3): x=1.0 m 处质点的振动方程并画出振动图。 

解: (1) 按所给条件, 取波动方程的一般形式为 

\[y = A \cos[2\pi(\frac{t}{T} - \frac{x}{\lambda}) + \varphi]\]

式中 \(\varphi\) 为坐标原点的振动初相, 由已知得:
\(\\\) 
\(\\\)
代入所给数据, 得 

\(\\\)
波动方程: \(y = 1.0 \cos[2\pi(\frac{t}{2.0} - \frac{x}{4.0})] - \frac{\pi}{2}\)
①

--- PAGE 016 ---
(2) 将t=1.0s代入①式得出此时刻波形方程: 

\[y=1.0\cos\left[2\pi\left(\frac{1.0}{2.0}-\frac{x}{4.0}\right)-\frac{\pi}{2}\right]=1.0\cos\left(\frac{\pi}{2}-\frac{\pi}{2}x\right)\]

∴ \(y = 1.0\sin{\frac{\pi}{2}}x\) ❷
由❷式可画出t=1.0s的波形图; 

(3) 将x=1.0m代入①式, 
得该处质点的振动方程: 

\[y = 1.0\cos{\left[2\pi\left(\frac{t}{2.0}-\frac{1.0}{4.0}\right)-\frac{\pi}{2}\right]}\]

由此作出其振动曲线如图:

--- PAGE 017 ---
例3: 简谐波在\(t=0\)时刻的波形图, 设此简谐波的频率为250Hz, 若波沿轴负方向传播, 求 (1) 该波的波动方程; (2) 画出\(t=T/8\)时刻的波形图; (3) 距原点O为100米处质点的振动方程与振动速度表达式。 

**解:** (1) 由图知 \(\lambda = 200 \, \text{m}\) 

\[ 
\begin{align*} u &= \lambda v = 200 \times 250 \\
&= 50000 \, \text{m·s}^{-1} \\
\omega &= 2\pi v = 2\pi \times 250 \\
&= 500 \, \pi \, \text{s}^{-1} 
\end{align*} 
\]

\(t=0\) 时, \(y_0 = A \cos \varphi = \frac{\sqrt{2}}{2} A\) 得: \(\varphi = \frac{\pi}{4}\) \(O\) 处质点向下运动: 

\(O\) 点振动方程: \(v_0 = -A \omega \sin \varphi < 0\) 

\(y_0 = A \cos (500 \pi t + \frac{\pi}{4})\) 

波动方程: \(y = A \cos \left[ 2\pi \left( 250 \, t + \frac{x}{200} \right) + \frac{\pi}{4} \right]\) \(m\)

--- PAGE 018 ---
(2) \(t = \frac{T}{8}\) 的波形 

将 \(t = 0\) 的波形向 \(-x\) 方向平移： 

\[\Delta x = u \times \frac{T}{8} = \frac{\lambda}{8} = \frac{25}{8} \text{ m}\]

(3) \(x=100\text{m}\) 处质点

振动方程： 

\[y_{100} = A \cos(500 \pi t + \frac{5}{4} \pi) \quad \text{m}\]

振动速度： 

\[v_{100} = \frac{\partial y_{100}}{\partial t} = -500 \pi A \sin(500 \pi t + \frac{5}{4} \pi) \text{ m} \cdot \text{s}^{-1}\]

--- PAGE 019 ---
思考题 

1. 频率为100Hz,传播速度为300m/s 的平面简谐波,波线上两点振动的相位差为π/3,则此两点相距（） 

(A) 1 m 

(B) 2 m 

(C) 0.5 m 

(D) 0.667 m 

2. 一列平面简谐波沿Ox轴正方向传播, t=0时刻的波形图如图所示, 则P处质点的振动方程为（）

(A) \(y_p = 0.10\cos(4\pi t+\pi/3)\) (SI) 

(B) \(y_p = 0.1\cos(4\pi t-\pi/3)\) (SI) 

(C) \(y_p = 0.10\cos(2\pi t+\pi/3)\) (SI) 

(D) \(y_p = 0.10\cos(2\pi t+\pi/6)\) (SI)

--- PAGE 020 ---
# 三、平面波的波动方程 

由平面简谐波的波函数 \(y(x,t) = A \cos[\omega(t-x/\mu)+\varphi_0]\) 

分别对t和x求二阶偏导数，得 

\[ \frac{\partial^2 y}{\partial t^2} = -A \omega^2 \cos[\omega(t-x/\mu)+\varphi_0] \]

\[ \frac{\partial^2 y}{x^2} = -A \frac{\omega^2}{\mu^2} \cos[\omega(t-x/\mu)+\varphi_2] \]

比较上面两式得， 

\[ \frac{\partial^2 y}{\partial x^2} - \frac{1}{\mu^2} \frac{\partial^2 y}{\partial t^2} = 0 \]

这就是一维波动微分方程，它是物理学中普遍地反映波动现象的一类二阶偏微分方程。这类偏微分方程深刻地揭示物理规律，因此称为数学物理方程。

--- PAGE 021 ---
波动微分方程的动力学导出过程: 

有一个完全柔软的均匀弦，沿水平直线绷紧，而后以某种方法激发，使弦在同一个平面上作小振动。 

- 取弦的平衡位置为x轴, 且令端点坐标为x=0与x=l. 

- 设u(x; t)是坐标为x的弦上一点在t时刻的(横向)位移, 在弦上隔离出长为dx的一小段(弦元), 可以把它看成是质点。 

- 分析弦元受力: 它在两个端点x及x+dx处受到张力的作用. 

因为弦是完全柔软的, 故只受到切向应力张力7的作用, 而没有法向应力. 同时, 略去了重力的作用. 由于只产生横向位移: 

\[\begin{align*} (T \sin \theta)_{x+dx} - (T \sin \theta)_x &= dm \frac{\partial^2 u}{\partial t^2}, \\ (T \cos \theta)_{x+dx} - (T \cos \theta)_x &= 0. \end{align*}\]

--- PAGE 022 ---
小振动近似：\(x+dx\)与\(x\)两点间任一时刻横向位移之差\(u(x+dx; t)-u(x; t)\)，与\(dx\)相比是一个小量 

在小振动近似下， 

\[ \sin \theta \approx \tan \theta = \frac{\partial u}{\partial x} \\ \cos \theta \approx 1 \]

\[ \tan \theta_1 = \left( \frac{\partial u}{\partial x} \right)_x, \quad \tan \theta_2 = \left( \frac{\partial u}{\partial x} \right)_{x+dx} \]

因此，有 

\[ (T)_{x+dx} - (T)_x = 0 \quad \text{即} \quad (T)_{x+dx} = (T)_x \]

说明\(T\)不随\(x\)变化，弦中各点的张力相等。 

\[ \rho dx \frac{\partial^2 u}{\partial t^2} = T \left[ \left( \frac{\partial u}{\partial x} \right)_{x+dx} - \left( \frac{\partial u}{\partial} \right)_x \right] = T \frac{\partial^2 u}{\partial x^2} dx \]

\[ T \frac{\partial^2 y}{\partial x^2} - \rho \frac{\partial^2 y}{\partial t^2} = 0 \quad \mu = \sqrt{\frac{T}{\rho}} - \frac{\partial^2 y}{\partial x^2} - \frac{1}{\mu^2} \frac{\partial^2 y}{\partial t^2} = 0 \]

--- PAGE 023 ---
## 8.3 波的能量 

波动过程 

质元由静止开始振动
质元也发生形变 

波动过程是能量的传播过程 

## 一.波的能量和能量密度 

以绳索上传播的横波为例：设波沿x方向传播，取线元 

\[ \Delta m = \rho \Delta x \]

线元的动能为 

\[ W_k = \frac{1}{2} \Delta m v^2 = \frac{1}{2} \Delta m \left( \frac{\partial v}{\partial t} \right)^2 \quad ① \]

线元的势能(原长为势能零点)为 

\[ W_p = T(\Delta l - \Delta x) \]

--- PAGE 024 ---
\[
\begin{align*}
\text{其中 } \Delta l &= \sqrt{(\Delta x)^2 + (\Delta y)^2} = \Delta x[1 + (\frac{\Delta y}{\Delta x})^2]^{1/2} \\
&= \Delta x[1 + (\frac{\partial y}{\partial x})^2]^{1/2} \approx \Delta x[1 + \frac{1}{2}(\frac{\partial y}{\partial x})^2]
\end{align*}
\]

\[
\begin{equation}
W_p \approx \frac{1}{2} T \Delta x \left( \frac{\partial y}{\partial x} \right)^2 \quad \text{②}
\end{equation}
\]

线元的机械能为 

\[
W = W_k + W_p
\]

③ 

将 \( T = u^2 \rho \) 和 \( y = A \cos[\omega(t - \frac{x}{u})] + \phi_0 \) 代入①、②、③ 

\[
W_k = \frac{1}{2} \rho \Delta x \left( \frac{\partial y}{\partial t} \right)^2 = \frac{1}{2} \rho \Delta x A^2 \omega^2 \sin^2[\omega(t - \frac{x}{u})] + \phi_0
\]

\[
W_p = \frac{1}{2} T \Delta x \left( \frac{\partial \dot{y}}{\partial x} \right)^2 = \frac{1}{2} p \Delta x A^2 \omega^2 \sin^2[\omega(t - \overline{x})] + \phi_0
\]

--- PAGE 025 ---
机械能 \(W = W_k + W_p = \rho \Delta x A^2 \omega^2 \sin^2[\omega(t - \frac{x}{u}) + \phi_0]\) 

讨论 

(1) 在波的传播过程中, 媒质中任一质元的动能和势能是同步变化的, 即 \(W_k = W_p\), 与简谐弹簧振子的振动能量变化规律是不同的; 如图所示, \(A\) 点质元的动能、势能同时达到最小; \(B\) 点质元的动能、势能同时达到最大;

--- PAGE 026 ---
(2) 质元机械能随时空周期性变化，表明质元在波传播过程中不断吸收和放出能量；因此，波动过程是能量的传播过程。 

## 二. 能流密度 

1. 能量密度 

设绳子的横截面为S，体密度为ρ，则线元单位体积中的机械能（能量密度）为 

\[ w = \frac{w}{\frac{S\Delta x}{\Delta t}} = \rho A^2\omega^2 \sin^2[\omega(t - \frac{x}{u}) + \varphi_0] = w(x, t) \]

- 平均能量密度 

\[ w = \frac{1}{T} \int_{0}^{T} w \, dt = \frac{1}{2} \rho A^2 \omega^2 \]

--- PAGE 027 ---
2. 能流 

在单位时间内通过一定截面的波动能量为能流 

\[ P = \frac{wu \Delta t S}{\Delta t} = wu S \]

在一个周期中的平均能流为 

\[ P = \frac{1}{T} \int_{0}^{T} P dt = wuS \]

- 能流密度 通过垂直于波线截面单位面积上的能流。 

大小：\(J = \frac{dP}{dS} = wu\) 

方向：波的传播方向 

矢量表示式：\(\vec{J} = w\vec{u}\)

--- PAGE 028 ---
波的强度——一个周期内能流密度大小的平均值。 

\[ I = \bar{J} = \frac{1}{T} \int_0^T Jdt = \frac{u}{T} \int_0^T wdt = uw = \frac{1}{2} \rho A^2 \omega^2 u \propto A^2 \] 

## 三. 平面波和球面波的振幅（不吸收能量） 

### 1. 平面波 

\[ W_1 = I_1 S_1 = \bar{w}_1 uS = \frac{1}{2} \rho A_1^2 \omega^2 uS \]
\[ W_2 = I_2 S_2 = \bar{w}_2 uS = \frac{1}{2} \rho A_2^2 \omega^2 uS \]
由
\[ W_1 = \bar{W_2} \]
得
\[ A_1 = A_2 \]
这表明平面波在媒质不吸收的情况下，振幅不变。

--- PAGE 029 ---
## 2. 球面波 

\[\text{由} \quad \frac{1}{2}\rho A_1^2\omega^2uS_1 = \frac{1}{2}\rho A_2^2\omega^2uS_2\]

\[\text{得} \quad A_1^2 \cdot 4\pi r_1^2 = A_2^2 \cdot 4\pi r_2^2 \\ A_1r_1 = A_2r_2\]

\[ \text{令 } Ar = A_0 \quad (A_0 \text{ 为离原点（波源）单位距离处波的振幅}) \\ \text{则球面简谐波的波函数为} \]

\[ y(r, t) = \frac{A_0}{r} \cos[\omega(t - \frac{r}{u}) + \varphi_0], \quad r > 0 \]

球面波的振幅在媒质不吸收的情况下, 随 \(r\) 增大而减小.

--- PAGE 030 ---
## 四.波的吸收 

吸收媒质,实验表明 

\[ \frac{dI}{I} = -\alpha I dx \]

\[ I = I_0 e^{-\alpha x} \]

α为介质吸收系数，与介质的性质、温度、及波的频率有关。

--- PAGE 031 ---
# 8.4 惠更斯原理

**惠更斯提出：**

(1) 行进中的波面上任意一点都可看作是的子波源；

(2) 所有子波源各自向外发出许多子波；

(3) 各个子波所形成的包络面，就是原波面在一定时间内所传播到的新波面。

**说明**

(1) 知某一时刻波前，可用几何方法决定下一时刻波前；

--- PAGE 032 ---
(2) 亦适用于电磁波，非均匀和各向异性媒质；

(3) 解释衍射、反射、折射现象；

由几何关系知：

\[\frac{\sin i}{\sin \gamma} = \frac{u_1 \Delta t}{u_2 \Delta t} = \frac{u_1}{u_2}\]

(反射)

(4) 不足之处（未涉及振幅，相位等的分布规律）。

--- PAGE 033 ---
# § 8.5 波的干涉

## 一. 叠加原理

**1. 波传播的独立性**

当几列波在传播过程中在某一区域相遇后再行分开，各波的传播情况与未相遇一样，仍保持它们各自的频率、波长、振动方向等特性继续沿原来的传播方向前进。

**2. 叠加原理**

在波相遇区域内，任一质点的振动，为各波单独存在时所引起的振动的合振动。

\[y = y_1 + y_2\]

注意 波的叠加原理仅适用于线性波的问题

--- PAGE 034 ---
## 二. 相干波与相干条件

- **干涉现象**

一般情况下，各个波的振动方向和频率均不同，相位关系不确定，叠加的合成波较为复杂。

当两列（或多列）相干波叠加的结果，其合振幅 \(A\) 和合强度 \(I\) 将在空间形成一种稳定的分布，即某些点上的振动始终加强，某些点上的振动始终减弱。——波的干涉

- **相干条件** 频率相同、振动方向相同、相位差恒定。

- **相干波** 满足相干条件的波

- **相干波源** 产生相干波的波源

--- PAGE 035 ---
## 三. 干涉规律

\[S_1 \quad y_{01} = A_1 \cos(\omega t + \varphi_1)\]

\[S_2 \quad y_{02} = A_2 \cos(\omega t + \varphi_2)\]

\[P \quad y_1 = A_1 \cos(\omega t - 2\pi \frac{r_1}{\lambda} + \varphi_1)\]

\[y_2 = A_2 \cos(\omega t - 2\pi \frac{r_2}{\lambda} + \varphi_2)\]

根据叠加原理可知, \(P\) 点处振动方程为

\[y = y_1 + y_2 = A \cos(\omega t + \phi)\]

合振动的振幅

\[A^2 = A_1^2 + A_2^2 + 2A_1 A_2 \cos[\varphi_2 - \varphi_1 - 2\pi \frac{r_2 - r_1}{\lambda}]\]

\(P\) 点处波的强度 \(I = I_1 + I_2 + 2\sqrt{I_1 I_2} \cos \Delta \varphi\)

--- PAGE 036 ---
**相位差**

\[
\Delta\varphi = (\varphi_2 - \varphi_1) - 2\pi \frac{r_2 - r_1}{\lambda}
\]

- 空间点振动的情况分析

\[
当 \Delta\varphi = (\varphi_2 - \varphi_1) - 2\pi \frac{r_2 - r_1}{\lambda} = \pm 2k\pi \quad k = 0,1,2, \dots
\]

\[
A_{\text{max}} = A_1 + A_2 \quad I_{\text{max}} = I_1 + I_2 + 2\sqrt{I_1 I_2}
\]

干涉相长

当 \(\Delta\varphi = (\varphi_2 - \varphi_1) - 2\pi \frac{r_2 - r_1}{\lambda} = \pm (2k+1)\pi\) \(k = 0,1,2, \dots\)

\[
A_{\text{min}} = |A_1 - A_2| \quad I_{\text{min}} = I_1 + I_2 - 2\sqrt{I_1 I_2}
\]

干涉相消

--- PAGE 037 ---
**讨论**

(1) 若 \(\varphi_1 = \varphi_2\)

\[
\begin{align*}
\delta &= r_1 - r_2 = \pm k \lambda, \quad k = 0, 1, 2, \dots & \text{干涉相长} \\
\delta &= r_1 - r_2 = \pm (2k + 1) \frac{\lambda}{2}, \quad k = 0, 1, 2, \dots & \text{干涉相消}
\end{align*}
\]

(2) 若 \(A_1 = A_2 = A\)

\[ A_{\text{max}} = 2A \quad I_{\text{max}} = 4I_0 \]
\[ A_{\text{min}} = 0 \quad I_{\text{min}} = 0 \]

干涉相长 / 干涉相消

从能量上看，当两相干波发生干涉时，在两波交叠的区域，合成波在空间各处的强度并不等于两个分波强度之和，而是发生重新分布。这种新的强度分布是时间上稳定的、空间上强弱相间具有周期性的一种分布。

--- PAGE 038 ---
# § 8.6 驻波

两列等振幅相干波相向传播时叠加形成驻波

### 一. 弦线上的驻波实验

波腹 / 波节

驻波条件: \(L = n \frac{\lambda}{2}\)，\(n = 1,2,3\dots\)

### 二. 驻波函数

\[
\begin{align*}
y_1 &= A \cos 2\pi(v t - \frac{x}{\lambda}) \\
y_2 &= A \cos 2\pi(v t + \frac{x}{\lambda})
\end{align*}
\]

--- PAGE 039 ---
\[
\begin{align*}
y &= y_1 + y_2 = A[\cos 2\pi (\nu t - \frac{x}{\lambda}) + \cos 2\pi (\nu t + \frac{x}{\lambda})] \\
&= (2A \cos 2\pi \frac{x}{\lambda}) \cdot \cos 2\pi \nu t = A'(x) \cos \omega t
\end{align*}
\]

(1) \(A'(x) = 2A\cos 2\pi\frac{x}{\lambda}\), 即驻波是各质点振幅按余弦分布的特殊谐振动;

当 \(\cos \frac{2\pi x}{\lambda} = 1\) 时

\[
\text{波腹}(A' = A'_{\text{max}}) : \quad x = k \frac{\lambda}{2}, \qquad k = 0, \pm 1, \pm 2, \dots
\]

当 \(\cos \frac{2\pi x}{\lambda} = 0\) 时

\[
\text{波节}(A' = A'_{\text{min}}) : \quad x = (2k+1) \frac{\lambda}{4}, \qquad k = 0, \pm 1, \pm 2, \dots
\]

--- PAGE 040 ---
相邻两波腹之间的距离：

\[ x_{k+1} - x_k = (k+1) \frac{\lambda}{2} - k \frac{\lambda}{2} = \frac{\lambda}{2} \]

相邻两波节之间的距离：

\[ x_{k+1} - x_k = [2(k+1) + 1] \frac{\lambda}{4} - (2k+1) \frac{\lambda}{4} = \frac{\lambda}{2} \]

(2) 所有波节点将媒质划分为长 \(\lambda/2\) 的许多段，每段中各质点的振动振幅不同，但相位皆相同；而相邻段间各质点的振动相位相反；即驻波中不存在相位的传播。

(3) 简正模式：特定的振动方式（波方程的解）称为系统的简正模式（或驻波的本征值）。

弦线上形成驻波的条件：\(L = n \frac{\lambda}{2}\) \((n=1, 2, 3, \dots)\)

驻波频率则为：\(v = \frac{u}{\lambda} = \frac{nu}{2L}\) \((n=1, 2, 3, \dots)\)

--- PAGE 041 ---
弦线上形成驻波的条件：

\[L = n \frac{\lambda}{2} \quad (n = 1, 2, 3, \dots)\]

\[v = \frac{u}{\lambda} = \frac{nu}{2L} \quad (n = 1, 2, 3, \dots)\]

Standing Waves Demo

环上的驻波

此时形成驻波的条件？

\[2\pi R = n\lambda \quad (n = 1, 2, 3, \dots)\]

--- PAGE 042 ---
例 平面简谐波 t 时刻的波形如图, 此波波速为 u, 沿 x 方向传播, 振幅为 A, 频率为 f。

求 (1) 以 D 为原点, 写出波函数;

(2) 以 B 为反射点, 且为波节, 若以 B 为 x 轴坐标原点, 写出入射波, 反射波方程;

(3) 以 B 为反射点求合成波, 并分析波节, 波腹的位置坐标。

解 (1) \(y(x,t) = A \cos[2\pi f(t - \frac{x}{u}) + \pi]\)

(2) \(y_{\lambda}(x,t) = A \cos[2\pi f(t - \frac{x}{u/2}) - \frac{\pi}{2}]\)

\[ y_{\text{反}}(x,t) = A \cos [2\pi f(t - \frac{x}{u/1})+\frac{\pi}{2}] \]

--- PAGE 043 ---
(3) \(y(x, t) = y_{\lambda} + y_{反} = 2A \cos \left( 2 \pi \frac{x}{u} + \frac{\pi}{2} \right) \cos 2 \pi f t\)
\[
= -2A \sin 2 \pi \frac{x}{u} \cos 2 \pi f t
\]

波腹：
\[
x = \frac{2k+1}{4} \cdot \frac{u}{f} = \frac{2k+1}{4} \lambda \quad k = -1, -2, -3, \dots
\]

波节：
\[
\left| \sin 2\pi \frac{x}{u} \right| = 0 \quad 2\pi \frac{x}{u} = k\pi
\]
\[
x = \frac{k}{2} \cdot \frac{u}{f} = \frac{k}{2} \lambda \qquad k = 0, -1, -2, -3, \dots
\]

--- PAGE 044 ---
# § 8.7 多普勒效应

由于观察者（接收器）或波源、或二者同时相对媒质运动，而使观察者接收到的频率与波源发出的频率不同的现象，称为多普勒效应。

## 一. 波源静止，观察者运动

\[f = \frac{u + v_o}{\lambda} = \frac{u + v_o}{u / f_0}\]

\[f = (1 + \frac{v_o}{u}) f_0\]

靠近 \(v_0 > 0\)；远离 \(v_0 < 0\)

--- PAGE 045 ---
## 二. 观察者静止, 波源运动

\[\lambda' = u T - v_s T = \lambda - v_s T = \frac{u - v_s}{f_0}\]

\[f = \frac{u}{\lambda'} = \frac{u}{u - v_s} f_0\]

靠近 \(v_s > 0\); 远离 \(v_s < 0\)

## 三. 波源和观察者同时运动

\[f = \frac{u + v_0}{u - v_s} f_0\]

符号正负的选择与上述相同

S 运动的前方波长变短

--- PAGE 046 ---
**讨论**

(1) 当波源或观察者在二者联线垂直方向上运动时，无多普勒效应。

(2) \(v_s > u\) 时，多普勒效应公式失去意义，此时形成冲击波。

\[ \text{马赫角} \quad \sin\theta = \frac{u}{v_s} \]

(3) 电磁波的多普勒效应

\[ f(\text{接近}) = \frac{1+\frac{v}{c}}{1-\frac{v}{c}} f_s \]

\[ f(\text{远离}) = \frac{1-\frac{v}{c}}{1+\frac{v}{c}} f_s \]

\(v\) 为光源和接收器的相对速度

(4) 应用：监测车辆行驶速度、测量血液流速、跟踪卫星等。

--- PAGE 047 ---
例 一警笛发射频率为1500 Hz 的声波，并以22 m/s 的速度向某一方向运动，一人以6 m/s 的速度跟踪其后。

求 该人听到的警笛发出的声音的频率以及在警笛后方空气中声波的波长？

解 观察者接收到的频率(波源和观察者同时运动)：

\[v_R = \frac{u+v_0}{u-v_S} v_0 = \frac{330+6}{330+22} \times 1500 = 1432 \text{ Hz}\]

警笛后方空气中声波的频率(观察者静止，波源运动)：

\[v = \frac{u}{u-v_S} v_0 = \frac{330}{330+22} \times 1500 = 1406 \text{ Hz}\]

警笛后方空气中声波的波长:
\[ \lambda = \frac{u}{v} = \frac{330+22}{1500} = 0.23 \text{ m}\]

--- PAGE 048 ---
# 第四次作业：

第七章 上册P272 7.5；7.7；7.15；7.17；7.25

第八章 下册P177 13.12；13.14；13.16；13.18；13.33
