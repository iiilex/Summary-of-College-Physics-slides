--- PAGE 001 ---
第3章 功和能

3.1 功

3.2 几种常见力的功

3.3 动能定理

3.4 势能 机械能守恒定律

3.5 能量守恒定律

--- PAGE 002 ---
### 3.1 功

\[
F
\] 
空间积累：功
\[
m
\]
时间积累：冲量

研究力在空间的积累效应
功、动能、势能、动能定理、机械能守恒定律。

## 一. 恒力的功

\[
A = Fs \cos\theta
\]

\[
A = F \cdot \bar{S}
\]

--- PAGE 003 ---
## 二. 变力的功

求质点M在变力作用下，沿曲线轨迹由a运动到b，变力作的功

F 在 dr 一段上的功：

\[dA = \vec{F} \cdot d\vec{r} \quad \text{cos} \theta \quad dA = \vec{F} \cdot d\vec{r}\]

F 在 ab 一段上的功

\[A = \int_{a(L)}^{b} \vec{F} \cdot d\vec{r}\]

在直角坐标系中

\[A = \int_{a(L)}^{b} (F_x dx + F_y dy + F_z dz)\]

在自然坐标系中

\[|\vec{dr}| = ds\]

\[A = \int_{a(L)}^{b} F \cos \theta ds\]

--- PAGE 004 ---
说明

(1) 功是标量, 且有正负

(2) 合力的功等于各分力的功的代数和

\[ A = \int_{a(L)}^{b} \mathbf{F} \cdot d\mathbf{r} = \int_{a(L)}^{b} (\mathbf{F}_1 + \mathbf{F}_2 + \cdots + \mathbf{F}_n) \cdot d\mathbf{r} \]

\[ = \int_{a(L)}^{b} \mathbf{F}_1^{b} \cdot d\mathbf{r} + \int_{a(L)}^{b} \mathbf{F}_2^{b} \cdot d\mathbf{r} + \cdots + \int_{a(L)}^{b} \mathbf{F}_n^{b} \cdot d\mathbf{r} \]

\[ = A_1 + A_2 + \cdots + A_n \]

(3) 一般来说, 功的值与质点运动的路径有关

解题时第一步永远是写出 dA
然后看"哪个变量在变", 把 dA 写成该变量的函数, 再积分。
建模能力

--- PAGE 005 ---
## 三. 功率

力在单位时间内所作的功，称为功率。

平均功率

\[P = \frac{\Delta A}{\Delta t}\]

当 \(\Delta t \to 0\) 时的瞬时功率
\[P = \lim_{\Delta t \to 0} \frac{\Delta A}{\Delta t} = \frac{dA}{dt}\]

\[P = \frac{\vec{F} \cdot d\vec{r}}{dt} = \vec{F} \cdot \vec{v} = F \nu \cos \theta\]

--- PAGE 006 ---
力的**大小**随时间变化的例子

**例1** 已知 \(m = 2\text{kg}\), 在 \(F = 12t\) 作用下由静止做直线运动

求 \(t = 0 \to 2\text{s}\) 内 \(F\) 作的功及 \(t = 2\text{s}\) 时的功率。

\[解 \quad \begin{vmatrix}\frac{F}{m}\end{vmatrix} = 6t = \frac{du}{dt} \rightarrow u = 3t^2 = \frac{dx}{dt}\]

\[A = \int_{0}^{x} F dx = \int_{0}^{t} F \cdot 3t^2 dt = \int_{0}^{2} 36t^3 dt = 144J\]

\[P = \bar{F} \cdot \bar{v} = 12t \cdot 3t^2 = 288W\]

--- PAGE 007 ---
**例2** 质量为10kg的质点,在外力作用下做平面曲线运动,该质点的速度为 \(\vec{v} = 4t^2 \vec{i} + 16 \vec{j}\), 开始时质点位于坐标原点。求在质点从 \(y = 16m\) 到 \(y = 32m\) 的过程中,外力做的功。

\[ \begin{aligned} &\text{解 } v_x = \frac{dx}{dt} = 4t^2 \quad & dx = 4t^2 dt \\ \\ &\text{解 } v_y = \frac{dy}{dt} = 16 \quad & y = 16t \\ \\ &\text{解 } v_y = \frac{dy}{dt} = 16t \quad & y = 16t \\ \end{aligned} \quad \begin{aligned} & y = 16t \quad & t = 1 \\ \\ & y = 32t \quad & t = 2 \end{aligned} \]

\[ \begin{aligned} F_x &= m\frac{dv_x}{dt} = 80t \quad & F_y &= m\frac{dv_y}{dt} = 0 \end{aligned} \]

\[ \Ang = \int F_x dx + F_y dy = \int_1^2 320t^3 dt = 1200 J \]

--- PAGE 008 ---
夹角变化的例子

例3已知用力 \(\vec{F}\) 缓慢拉质量为\(m\)的小球, \(\vec{F}\) 保持方向不变

求 \(\theta = \theta_0\) 时, \(\vec{F}\) 作的功。

\[\begin{cases} F - T \sin \theta = 0 \\ T \cos \theta - mg = 0 \end{cases}\]

\[F = mg \tan \theta\]

\[A = \int \vec{F} \cdot d\vec{r} = \int F \cos \theta \, ds\]

\[= \int_0^{\theta_0} mg \tan \theta \cos \theta \, d\theta\]

\[= \int_{0}^{\theta_0} mg L \tan \theta \cos \theta d\theta\]

\[= mgL(1 - \cos \theta_0)\]

--- PAGE 009 ---
一.重力的功

重力 \(mg\) 在曲线路径 \(M_1M_2\) 上的功为

\[ A = \int_{M_1(1)}^{M_2} F_z dz = \int_{Z_1(1)}^{Z_2} (-mg) dz \]
\[ = mg (Z_1 - Z_2) \]

重力所作的功等于重力的大小乘以质点起始位置与末了位置的高度差。

结论

(1) 重力的功只与始、末位置有关，而与质点所行经的路径无关。

(2) 质点上升时，重力作负功；质点下降时，重力作正功。

--- PAGE 010 ---
# 书中例题3.2(p.98) (重点)

一条长L,质量M的均匀柔绳,A端挂在天花板上,自然下垂,将B端沿铅直方向提高到与A端同高处。求:该过程中重力所作的功。解:提升高度y时,提的链长y/2

提起部分的质量

\[\frac{M}{L} \cdot \frac{1}{2} y\]

dy上的元功为:

\[dA = -\frac{1}{2} \frac{M}{L} gy dy\]

\[A = \int_{0}^{L} dA = \int_{0}^{L} -\frac{1}{2} \frac{M}{L} gy dy = -\frac{1}{4} MgL\]

--- PAGE 011 ---
## 二. 弹性力的功

弹簧弹性力

\[F = -kx^2\]

由 \(x_1\) 到 \(x_2\) 路程上弹性力的功为

\[A = \int_{x_1}^{x_2} -kxdx = \frac{1}{2}kx_1^2 - \frac{1}{2}kx_2^2\]

弹性力的功等于弹簧劲度系数乘以质点始末位置弹簧形变量平方之差的一半。

## 结论

1. 弹性力的功只与始、末位置有关, 而与质点所行经的路径无关。

2. 弹簧的变形减小时, 弹性力作正功; 弹簧的变形增大时, 弹性力作负功。

--- PAGE 012 ---
### 三. 万有引力的功

\(F\) 在位移元 \(dr\) 上的元功为
\[
dA = F \cos \theta \, dr \quad F = G \frac{mM}{r^2}
\]
\[
dr = |dr| \cos(\pi - \theta) = -|dr| \cos \theta
\]

\[
dA = -G \frac{mM}{r^2} dr
\]

万有引力 \(F\) 在全部路程中的功为

\[
A = \int_{r_1(L)}^{r_2} -G \frac{mM}{r^2} \, dr = GmM \left(\frac{1}{r_2} - \frac{1}{r_1}\right)
\]

### 结论

(1) 万有引力的功，也是只与始、末位置有关，而与质点所行经的路径无关。

--- PAGE 013 ---
(2) 质点移近质点时，万有引力作正功；质点A远离质点O时，万有引力作负功。

## 四. 摩擦力的功

摩擦力 \(\vec{F}\) 在这个过程中所作的功为

\[ A = \int_{M_1(L)}^{M_2} F \cos \alpha ds \]

\[ F = \mu mg \]

摩擦力方向始终与质点速度方向相反

\[ A = -\mu mgs \]

### 结论

摩擦力的功，不仅与始、末位置有关，而且与质点所行经的路径有关。

--- PAGE 014 ---
例5（重点）

蓄水池面积S，水深h，水面距地面H，水的密度为ρ。

求：抽出水需要作多少功？

解：离地面x处，深dx的一层水的

质量dm=ρSdx，将dm水提到路面所需的功：

\[dA = gxdm = \rho S g x dx\]

\[A = \int_H^{H+h} \rho S g x dx = \frac{1}{2} \rho S g x^2 \Big|_{H}^{H+h} = \rho g SHh + \rho g S \frac{h^2}{2}\]

抽水做功 = 把全部水的质心提升到地面
讨论：微元思想 / 质心思想

--- PAGE 015 ---
例6

风力F作用于向北运动的船，风力方向变化的规律是：θ = Bs，其中s为位移，B为常数，θ为F与S间的夹角。如果运动中，风的方向自南变到东，
求：风力作的功。

解：元功： \(dA = Fds \cos\theta\); 其中 \(θ = Bs\), \(ds = dθ/B\)
积分限：风向由南变到东，则θ由0变到π/2

\[A = \int_{0}^{\pi/2} \frac{F \cos\theta}{B} d\theta = \left. \frac{F \sin\theta}{B} \right|_{0}^{\pi/2} = F/B\]

小结：

\(A = Fs\cos\theta\)

解题时写出元功dA的表达式，弄清做功过程中是哪个参数在变化，就最终建立dA与这个参数的微分表达式，再确定这个参数的初、末值积分。

--- PAGE 016 ---
## 思考题：

如图所示，作用于一质点的力随质点位移的变化为 \(\vec{F} = y\vec{i} + 3x^2\vec{j}(N)\)，请分别计算该力沿oab及ob所做的功。

--- PAGE 017 ---
## 3.3 动能定理

## 一. 质点动能定理

\[dA = \mathbf{F} \cdot d\mathbf{r} = m \frac{d\mathbf{r}}{dt} \cdot d\mathbf{r} = m\mathbf{v} \cdot d\mathbf{v} = md\mathbf{v} du\]

\[\int dA = \int_{v_1}^{v_2} mu dv\]

\[A = \frac{1}{2} mv_2^2 - \frac{1}{2} mv_1^2 = E_{k2} - E_{k1}\]

作用于质点的合力在某一路程中对质点所作的功，等于质点在同一路程的始、末两个状态动能的增量。

--- PAGE 018 ---
说明：

1. 动能是标量，是能量的一种表现形式。

2. 动能定理说明了作功与动能的关系。

即：合力作正功时 (A>0)，质点动能增加；【加速】
  合力作负功时 (A<0)，质点动能减少。 【减速】

3. 方程左边的结果取决于F的具体函数形式，与力对质点的作用过程相关。

· 功是过程量；

方程右边与过程无关，只由始末运动状态确定。

· 动能是状态量。

4. 动能定律只用于惯性系。

--- PAGE 019 ---
书中例题3.5 P103

物体的质量为m, 弹簧劲度系数为k, A板及弹簧质量不计, 求自弹簧原长O处, 突然无初速度地加上物体M时, 弹簧的最大压缩量。

设弹簧最大压缩量为 \(\lambda_{\text{max}}\),

显然物体从起始位置 \(x_1=0\), 移动到末了位置 \(x_2=\lambda_{\text{max}}\) 的过程中, 重力和支承力的功分别为

\[A_1 = \mathrm{mg}\lambda_{\text{max}}\]

\[A_2 = \int_0^{\lambda_{\text{max}}}(-kx) \, \mathrm{d}x = -\frac{1}{2} k\lambda_{\text{max}}^2\]

可见重力对物体作正功, 支承力对物体作负功.
按题意物体在起始位置 \(x_1=0\) 及末位置 \(x_2=\lambda_{\text{max}}\) 处的速度均为零, 根据动能定理, 有

\[\mathrm{mg}\lambda_{\text{max}} - \frac{1}{2} k\lambda_{\text{max}}^2 = 0 - 0\]

\[\lambda_{\text{max}} = 2 \frac{\mathrm{mg}}{k}\]

如果将重物缓慢放下, 使物体达到静平衡,
这时所引起的弹簧压缩量设为 \(\lambda_{\text{sl}}\), 则应有

\[\lambda_{\text{sl}} = \mathrm{mg} \quad \text{故} \quad \lambda_{\text{sl}} = \frac{\mathrm{mg}}{k}\]

--- PAGE 020 ---
# 二. 质点系动能定律

把质点动能定理应用于质点系内所有质点并把所得方程相加有:

\[ \sum_i A_i = \sum_i \frac{1}{2} m_i v_{i2}^2 - \sum_i \frac{1}{2} m_i v_{i1}^2 \]

\[ \sum_i \bar{A_i} = \sum_i A_{i外} + \sum_i \bar{A_{i内}} \]

## 讨论

(1) 内力和为零,内力功的和不一定为零

\[ \bar{f}_1 = -\bar{f}_2 \]

\[ \sum f = 0 \]

\[ A_1 = -f_1L \]

\[ A_2 = f_2S \]

\[ \sum A = -f_1(L-S) \]

--- PAGE 021 ---
(2)内力的功能能改变系统的动能

∴功是标量,其和为代数和。

内力总是成对出现的,按照牛顿第三定律,这一对力的矢量和为0,但这一对力所作的功能的和不一定为0。

例:炸弹爆炸,过程内力和为零,但内力所做的功转化为弹片的动能。

--- PAGE 022 ---
## 书中例题3.11（p111）（重点）

例 长为\(l\)的均质链条，部分置于水平面上，另一部分自然下垂，已知链条与水平面间静摩擦系数为\(\mu_0\)，滑动摩擦系数为\(\mu\)

求 (1) 满足什么条件时，链条将开始滑动

(2) 若下垂部分长度为\(b\)时，链条自静止开始滑动，当链条末端刚刚滑离桌面时，其速度等于多少？

解 (1) 以链条的水平部分为研究对象，设链条每单位长度的质量为\(\rho\)，沿铅垂向下取\(Oy\)轴。

设链条下落长度\(y=b_0\)时，处于临界状态

\[ \rho b_0 g - \mu_0 \rho (l - b_0) g = 0 \quad b_0 = \frac{\mu_0}{1 + \mu_0} l \]

当 \(y>b_0\)，拉力大于最大静摩擦力时，链条将开始滑动。

--- PAGE 023 ---
(2) 以整个链条为研究对象，链条在运动过程中各部分之间相互作用的内力的功之和为零，

\[重力的功 A = \int_{b}^{l} \rho y g dy = \frac{1}{2} \rho g (l^2 - b^2)\]

\[摩擦力的功 A' = -\int_{b}^{l} \mu \rho (l - y) dy = -\frac{1}{2} \mu \rho g (l - b)^2\]

根据动能定理有

\[\frac{1}{2}\rho g (l^2 - b^2) - \frac{1}{2}\mu g (l - b)^2 = \frac{1}{2}\rho l v^2 - 0\]

\[v = \sqrt{\frac{g}{l} (l^2 - b^2) - \frac{\mu g}{l} (l - b)^2}\]

--- PAGE 024 ---
# 书中例题3.12

水平面内有一半径为R的圆，在圆内离圆心O距离为S处有一质量很大、可视为固定的力心O'，力心对单位质量的有心引力为μr，r为力心到质量为m的质点Q的位矢大小，质点Q被限制在圆周上运动。

求：（1）质点Q从B点由静止出发转过ϕ角有心力所做的功

（2）质点通过第二象限所经历的时间

\[dA = Fdr\cos\theta = FRd\phi\sin\alpha\]

由正弦定理：

\[ \frac{\sin\alpha}{S} = \frac{\sin(\pi - \phi)}{r} = \frac{\sin\phi}{r} \]

\[ \therefore \sin\alpha = \frac{S}{r} \sin\phi \]

\[ dA = \mu r R d\phi - \frac{S}{r} \sin\phi = \mu r R S \sin\phi d\phi \]

\[ A = \int_{0}^{\phi} \mu\mu R S \sin\phi \, d\phi \]

\[ = -\mu\mu R S \cos\phi \Big|_{0}^{\phi} \]

\[ = m\mu R S (1-\cos \phi) \]

--- PAGE 025 ---
(2) 由动能定理

\[m\mu RS(1 - \cos \varphi) = \frac{1}{2} mR^2 \left( \frac{d\varphi}{dt} \right)^2 \quad \frac{d\varphi}{dt} = \sqrt{\frac{2\mu S}{R}} (1 - \cos \varphi) = 2 \sqrt{\frac{\mu S}{R}} \sin \frac{\varphi}{2}\]

\[dt = \frac{d\varphi}{2 \sqrt{\frac{\mu S}{R}} \sin \frac{\varphi}{2}} = \frac{1}{2} \sqrt{\frac{R}{\mu S}} \frac{d\varphi}{\sin \frac{\varphi}{2}}\]

两边同时积分, 通过第二象限是 \(\varphi\) 由 \(\frac{\pi}{2}\) 变到 \(\pi\)

\[\int_{t_1}^{t_2} dt = \int_{\pi/2}^{\pi} \frac{1}{2} \sqrt{\frac{R}{\mu S}} \frac{d\varphi}{\sin \pi \varphi}\]

\[t_2 - t_1 = \frac{1}{2} \sqrt{\frac{R}{\mu S}} \int_{\pi/2}^{\pi} \frac{d\varphi}{2 \sin \frac{\varphi}{2}} = \sqrt{\frac{R}{\mu S}} \ln \tan \frac{\varphi}{4} \int_{\pi/2}^{\pi} = 0.88 \sqrt{\frac{R}{\mu S}}\]

--- PAGE 026 ---
### 3.4 势能 机械能守恒定律

## 一. 保守力

如果力所做的功与路径无关，而只决定于物体的始末相对位置，这样的力称为保守力。

保守力沿闭合路径一周所做的功为零。

即

\[ \int_{L} \vec{f} \cdot d\vec{r} = 0 \]

例如重力、万有引力、弹性力都是保守力。

作功与路径有关的力称为非保守力。

例如：摩擦力

--- PAGE 027 ---
## 二. 势能

在保守力场中，质点的始末位置一定，力作的功便确定。

根据动能定理，作功的结果是使质点的动能发生变化。这说明在保守场中，两点之间的能量不同，而且这一能量只与位置有关。当质点的位置改变时，这一能量便释放出来，转变成质点的动能。——这就是保守场的势能。

选空间上的一点 \(M_0\) 为势能0点；由空间上M点到势能0点 \(M_0\) 过程中，保守力所作功的大小为该点的势能。

\[E_p = \int_{M_0}^{M_0} \mathbf{F} \cdot d\mathbf{r}\]

注意：势能的大小由相对位置决定，没有绝对大小；势能0点的选取是任意的。

--- PAGE 028 ---
## 1. 重力势能

\[E_p = \int_z^0 (-mg)dz = mgy\]

- 重力势能与x成正比, 重力势能0点的选择可以是任意的。

--- PAGE 029 ---
## 2. 弹性势能

\[E_p = \int_{x}^{0} (-\mathbf{k}x) \, dx = \frac{1}{2} \mathbf{k}x^2\]

注意：

- 因为弹性势能与\(x^2\)成正比, \((x+\Delta x)^2\)与\(x^2+\Delta x^2\)不同, 弹簧的势能0点要选原长位置时, 才有这么简捷的表达式。故对于弹簧的弹性势能, 势能0点通常选弹簧的原长。

- 当保守力作正功时, 质点动能增加, 势能减少:
【势能一动能】

- 当保守力作负功时, 质点动能减少, 势能增加:
【动能一势能】

--- PAGE 030 ---
书中例题3.5 ( p103)

物体质量 m, 弹簧的劲度系数为k, 自弹簧原长, 无初速度加上物体。
求: 弹簧的最大压缩量 y_{max}。

解: 重力和弹簧的弹性力都是保守力。

初: 动能 = 0; 重力势能 = mgy_{max}, 弹性势能 = 0

末: 动能 = 0; 重力势能 = 0, 弹性势能 = 1/2 ky_{max}^2

重力势能转换成弹性势能

\[ 
\begin{gather*} 
\tfrac{mg y_{\text{max}} = 1/2 ky_{\text{max}}^2}{y_{\text{max}} = 2mg/k} \\ 
\end{gather*} 
\]

在整个运动过程中, 重力势能减小, 动能增加, 弹性势能增加; 当 \(N=mg\) 时, 物体受力为 0, 但这时物体具有动能, 所以要继续压缩弹簧, 直到动能为 0, 这时 \(N > mg\), 物体在 \(N\) 的作用下往回运动, 直到所有的弹性势能转换成重力势能才停下来 (动能为 0)。物体在力的平衡点处 (\(N=mg\)) 上下振动。

--- PAGE 031 ---
3. 万有引力势能

\[E_p = \int_r^\infty (-\frac{GM}{r^2}) \mathrm{d}r = -G \frac{mM}{r}\]

例如

等着,

在质量为\(M\)、半径为\(R\)、密度为\(\rho\)的球体的万有引力场中

(1) 质点在球外任一点\(C\)，与球心距离为\(x\)，质点受到的万有引力为:

\[f = G \frac{Mm}{x^2}\]

\[E_p = \int_x^\infty -G \frac{Mm}{x^2} dx = -G \frac{Mm}{x}\]

--- PAGE 032 ---
(2) 质点在球内任一点C, 与球心距离为\(x\), 质点受到的万有引力为

\[f = G \frac{4}{3} \pi \rho m x\]

\[E_p = \int_x^R -G \frac{4}{3} \pi \rho m x dx + \int_R^\infty -G \frac{Mm}{x^2} dx\]

\[= -G \frac{2}{3} \pi \rho m (R^2 - x^2) - G \frac{Mm}{R}\]

\[= -GMm \left( \frac{3R^2 - x^2}{2R^3} \right)\]

- 在保守力场中, 质点从起始位置 1 到末了位置 2, 保守力的功 A 等于质点在始末两位置势能增量的负值

--- PAGE 033 ---
\[A = - (E_{p2} - E_{p1}) = -\Delta E_{p}\]

**说明**

(1) 由于势能零点可以任意选取，所以某一点的势能值是相对的。

(2) 保守力场中任意两点间的势能差与势能零点选取无关。

## 三. 势能曲线

质点的势能与位置坐标的关系可以用图线表示出来。

--- PAGE 034 ---
由势能函数求保守力

\[E_p = E_p(x, y, z) \quad \mathrm{d}E_p = \frac{\partial E_p}{\partial x} \mathrm{dx} + \frac{\partial E_p}{\partial y} \mathrm{dy} + \frac{\partial E_p}{\partial z} \mathrm{dz}\]

\[\mathrm{d}A = \mathbf{F} \cdot \mathrm{d}\mathbf{r} = F_x \mathrm{dx} + F_y \mathrm{dy} + F_z \mathrm{dz}\]

\[\mathrm{d}A = \mathbf{-d}E_p \quad \qquad \bar{F} = -\left(\frac{\partial E_p}{\partial x}\bar{\mathbf{r}} + \frac{\partial E_p}{\partial y}\bar{\mathbf{j}} + \frac{\partial E_p}{\partial z}\bar{\mathbf{k}}\right)\]

- 势能曲线上某点斜率的负值, 就是该点对应的位置处质点所受的保守力。

- 势能与其对应的保守力的微分关系: 保守力是势能的负梯度。

\[\nabla = \frac{\partial}{\partial x}\vec{i} + \frac{\partial}{\partial y}\vec{j} + \frac{\partial}{\partial z}\vec{k} \qquad \mathbf{F} = -\nabla E_p\]

--- PAGE 035 ---
稳定平衡

\[ \frac{dE}{dx} = 0 \]

\[ \frac{d^2 E_p}{dx^2} > 0 \]

不穩定平衡

\[ \frac{dE}{dx} = 1 \]

\[ \frac{d^2 E_p}{dx^2} < 1 \]

隨遇平衡

\[ \frac{d^2 E_p}{dx^2} = 0 \]

\[ \frac{d^2 E_p}{dx^2} = 1 \]

--- PAGE 036 ---
\[ \text{例} \quad \overline{F} = x^2 y^2 \overline{t} + x^2 y^2 \overline{j} \quad \text{是不是保守力?} \]

**解 如果是保守力，则**

\[ \begin{align*} \frac{\partial F_x}{\partial y} &= -\frac{\partial^2 E_p}{\partial x \partial y} \\[4pt] \frac{\partial F_y}{\partial x} &= -\frac{\partial^2 E_p}{\partial y \partial x} \end{align*} \]

\[ \frac{\partial F_x}{\partial y} \]

\[ \frac{\partial F_y}{\partial x} \]

\[ \text{不是保守力} \]

**三维判断保守力=交叉偏导是否相等**

\[ F = 2xy i + x^2 j \quad \text{呢?} \]

--- PAGE 037 ---
## 四. 机械能守恒定律

对质点系: 
\[ A_{外}+A_{内}=\Delta E_{k} \]

\[ A_{外} + A_{内}+A_{非内}= \Delta E_k \]

\[ A_{外} - \Delta E_p + A_{非内} = \Delta E_k \]

\[ A_{外} + A_{{\r{非内}}} = \Delta E_k + \Delta E_p = \Delta E \quad \text{机械能增量} \]

当 \(A_{外}+A_{非内}=0 \quad \Delta E=0\)

机械能守恒定律

说明

(1) 守恒条件 \(A_{外}+A_{非内}=0\)

(2) 守恒定律是对一个系统而言的

(3) 守恒是对整个过程而言的, 不能只考虑始末两状态

--- PAGE 038 ---
例 把一个物体从地球表面上沿铅垂方向以第二宇宙速度

\[
v_0 = \sqrt{\frac{2GM}{R_e}} e \quad \text{发射出去, 阻力忽略不计,}
\]

求 物体从地面飞行到与地心相距 \(nR_e\) 处经历的时间。

解 根据机械能守恒定律有：

\[
\frac{1}{2} mv_0^2 - G \frac{M_e m}{R_e} = \frac{1}{2} mv^2 - G \frac{M_e m}{x} \qquad \nu = \sqrt{\frac{2GM_e}{x}}
\]

\[
\nu = \frac{dx}{dt} \quad \rightarrow \quad \frac{d x}{d t} = \frac{dx}{\nu} = \frac{1}{\sqrt{2GM_e}} \sqrt{x} dx
\]

\[
\int_{0}^{t_{1}} dt = \int_{R_{e}}^{nR_{e}} \frac{1}{\sqrt{2GM_{e}}} \sqrt{x} dx \qquad t_{1} = \frac{2}{3\sqrt{2GM_{e}}} R_{e}^{3/2} \left( n^{3/2} - 1 \right)
\]

--- PAGE 039 ---
例 用弹簧连接两个木板 \(m_1\)、\(m_2\)，弹簧压缩 \(x_0\)。

求 给 \(m_2\) 上加多大的压力能使 \(m_1\) 离开桌面？

解 整个过程只有保守力作功，机械能守恒

\[
\begin{align*}
x_0 &= \frac{m_2 g}{k} \quad & x_1 &= \frac{F}{k} \quad & x_2 &= \frac{m_1 g}{k} \\
\frac{1}{2}k(x_0 + x_1)^2 &= \frac{1}{2}k x_2^2 + m_2 g(x_0 + x_1 + x_2) \\
F &= (m_1 + m_2) g
\end{align*}
\]

--- PAGE 040 ---
## 书中例题3.15（p126）

物体M悬于弹簧上，弹簧的弹性系数为k，弹簧的原长与圆环的半径相等。不计摩擦力. 求：物体自弹簧的原长无初速度的沿圆环滑至最低点B时所获得的动能。

解：不计摩擦力，所以圆环只起到约束的作用。

重力和弹性力都是保守力。

选择B点为重力势能0点

初：重力势能=mg(R+cos60°), 弹性势能=0, 动能=0
末：重力势能=0, 弹性势能=kR²/2, 动能=Ek

\[
\begin{aligned}
E_k + kR^2/2 &= mg(R + \cos 60^\circ) \\
Ek &= \frac{3}{2}mgR - kR^2/2
\end{aligned}
\]

--- PAGE 041 ---
### 3.5 能量守恒定律

能量不能消失，也不能创造，只能从一种形式转换为另一种形式。对一个封闭系统来说，不论发生何种变化，各种形式的能量可以互相转换，但它们总和是一个常量。这一结论称为能量转换和守恒定律。

### 讨论

1. 能量守恒定律可以适用于任何变化过程

2. 功是能量交换或转换的一种度量

3. 机械能守恒定律是普遍的能量守恒定律在机械运动范围内的体现

--- PAGE 042 ---
作业：p.136
3.11 3.17 3.18 3.19

5. 一人从10 m深的井中匀速地提水，起始桶中装有10kg的水，由于水桶底部均速地漏水，每升高1m要漏掉0.2kg水。问水桶被均速地从井中提到井口，人所做的功。
