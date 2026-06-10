--- PAGE 001 ---
# 质点的运动规律和刚体定轴转动规律的对比(一)

|  | 质点运动 | 刚体定轴转动 |
|---|---|---|
| 速度 | \({\vec{v}}={\frac {{\vec {d}}{\vec {r}}}{dt}}\) | 角速度<br/>\({\boldsymbol {\omega }}={\frac {{\boldsymbol {d}}\theta }{dt}}\) |
| 加速度 | \({\vec {a}}={\frac {{\vec {d}}{\vec {v}}}{dt}}\) | 角加速度<br/>\({\boldsymbol {\alpha }}={\frac {{\boldsymbol {d}}{\boldsymbol {\omega }}}{dt}}\) |
| 质量 | \(m\)，力 F | 转动惯量 J, 力矩 M |
| 力的功 | \(A=\int _{a}^{b}{\vec {F}}\cdot d{\vec {r}}\) | 力矩的功<br/>\(A=\int _{\theta _{a}}^{\theta _{b}}Md\theta\) |
| 动能 | \(E_{k}=\frac {1}{2}mv^{2}\) | 转动动能<br/>\(E_{k}=\frac {1}{2}J\omega ^{2}\) |
| 势能 | \(E_{p}=mgh\) | 转动势能<br/>\(E_{p}=mgh_{c}\) |

## 角量与线量的关系

\(s=r\theta\) \(v=r\omega\) \(a_{\tau }=r\beta\) \(a_{n}=r\omega ^{2}\)

--- PAGE 002 ---
# 质点的运动规律和刚体定轴转动规律的对比(二)

| 质点运动 | 刚体定轴转动 |
|---|---|
| 牛顿定律 \({\vec F} = m\vec a\) | 转动定律 \({\dot M} = J\vec a\) |
| 动量定理 \(\int_{0}^{t} \vec F dt = m_{i}\vec v_{i} - m_{i}\vec v_{i0}\) | 角动量定理 \(\int_{0}^{t} M dt = J\omega - J_{0}\omega_{0}\) |
| 动量守恒 \(\sum_{i} m_{i}\vec v_{i} = \sum_{i} m_{i}\vec v_{i0}\) | 角动量守恒 \(\vec J\vec \omega = \vec J_{0}\vec \omega_{0}\) |
| 动能定理 \(A = \frac{1}{2} mv^2 - \frac{1}{2} mv_0^2\) | 转动动能定理 \(A = \frac{1}{2} J\omega^2 - \frac{1}{2} J\omega_0^2\) |
| 机械能守恒 \(E_k + E_p = \text{const}\) | 机械能守恒 \(E_k + E_p = \text{const}\) |

--- PAGE 003 ---
# 第6章 刚体力学

6.1 刚体运动的描述
6.2 刚体绕定轴转动的转动定律
6.3 绕定轴转动刚体的动能
6.4 刚体的动量矩和动量矩守恒定律

--- PAGE 004 ---
## 6.1 刚体运动的描述

### 一、刚体和自由度的概念

- 如果需要研究物体的转动，就不能忽略它的形状和大小而把它简化为质点来处理。但如果物体的形状和转动不能忽略，而形变可以忽略。我们就得到实际物体的另外一个抽象的质点组——刚体(rigid body)，即形状和大小完全不变的物体。

- 刚体是组内任意两质点间的距离保持不变的质点组。

- 刚体和质点都是对实际物体的抽象。刚体考虑了物体的体积效应，但忽略了物体的形变。与质点相比，刚体更加接近实际物体。

--- PAGE 005 ---
自由度: 确定一个物体的位置所需要的独立坐标数。

质点的位置: x, y, z三个空间坐标, 3个自由度。

刚体的运动: 任意点的平动+绕该点的转动

点的平动有3个自由度;

绕定点转动有3个自由度（三个方位角中的两个+绕转动轴转过的角度）;
因此，自由刚体一共6个自由度。

--- PAGE 006 ---
## 二. 刚体的平动

刚体运动时, 若在刚体内所作的任一条直线都始终保持和自身平行 —— 刚体平动

- 平动的特点

(1) 刚体中各质点的运动情况相同（运动轨迹、速度、加速度）

\[ \vec{r}_A = \vec{r}_B + \overrightarrow{AB} \]

\[ \Delta \vec{r}_A = \Delta \vec{r}_B \]

\[ \begin{aligned} \vec{u}_A &= \vec{v}_B \\ \vec{a}_A &= \vec{a}_B \end{aligned} \]

(2) 刚体的平动可归结为质点运动（物体的质心运动）

--- PAGE 007 ---
## 书中例题5.1(P.182)

曲柄连杆机构是将转动转换为平动的机械机构，装置如图，曲柄长度为r，与x轴的夹角φ=ωt，其中ω为常量。求：T形连杆在t时刻的速度和加速度。

解：T形连杆的运动为平动，∵连杆上任意点的速度和加速速度都相同。以杆上M点为研究对象：

\(x = r \cos \omega t\)

对时间t求导得速度和加速度：

\(v = -r \omega \sin \omega t\)

\(a = -r \omega^2 \cos \omega t\)

--- PAGE 008 ---
## 三. 刚体绕定轴转动

刚体内各点都绕同一直线(转轴)作圆周运动—刚体转动
转轴固定不动 — 定轴转动

--- PAGE 009 ---
### 1. 描述刚体绕定轴转动的角量

刚体绕一固定轴转动，它只有一个自由度，转过的角度 \(\theta\) 称为角位移，它是时间的单值函数。

角位移的单位: rad（弧度）；角位移的方向: 右手定则，符合右手定则的方向为"+"；反之为"-"

\(θ = f(t)\)

这是刚体绕定轴转动的运动学方程

--- PAGE 010 ---
角速度: 描述刚体转动快慢的物理量。单位: rad/s (弧度/秒); 方向: 右手定则

\[ \text{角速度是角位移随时间的变化率} \quad \omega = \frac{d\theta}{dt} = f'(t) \]

\[ \omega = \frac{\pi n}{30} \text{ n称为转数，r/min} \]

角加速度: 描述刚体角速度变化快慢的物理量。单位: rad/s²

\[ \text{角加速度是角速度随时间的变化率} \quad \beta = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2} = f''(t) \]

任意时刻, 刚体的角速度和角加速度是唯一的

--- PAGE 011 ---
## 2. 定轴转动刚体上各点的速度和加速度——角量与线量的关系

任意点都绕同一轴作圆周运动, 且 ω, β 都相同

\[
\begin{align*}
v &= r' \omega \\
a_n &= r' \omega^2 \\
a_\tau &= \frac{dv}{dt} = r' \beta
\end{align*}
\]

--- PAGE 012 ---
M点加速度a的大小

\[| \vec{a} | = r_M \sqrt{\beta^2 + \omega^4}\]

M点加速度的方向由a与半径 OM的夹角来确定

\[\tan \alpha = \left| \frac{a_{\tau}}{a_{n}} \right| = \frac{\beta}{\omega^2}\]

在确定时刻，(1) 转动刚体上的各点速度和加速度大小都与该点到转轴的距离成正比；(2) \(\alpha\) 角对刚体内所有各点都相同

--- PAGE 013 ---
考虑方向后, 位移与角位移的关系:

\[ \vec{S} = \vec{\theta} \times \vec{r} \]

速度与角速度的矢量关系式

\[ \vec{v} = \frac{d\vec{r}}{dt} = \vec{\omega} \times \vec{r} \]

加速度与角加速度的矢量关系式

\[ \vec{a} = \frac{d\vec{v}}{dt} = \frac{d(\vec{\omega} \times \vec{r})}{dt} = \frac{d\vec{\omega}}{dt} \times \vec{r} + \vec{\omega} \times \frac{d\vec{r}}{dt} = \vec{\beta} \times \vec{r} + \vec{\omega} \times \vec{v} \]

\[ a_{\tau} = \vec{\beta} \times \vec{r} \quad \vec{a}_{n} = \vec{\omega} \times \vec{v} \]

--- PAGE 014 ---
# 6.2 力矩 刚体绕定轴转动的转动定律

## 一. 刚体的力矩

- 力 → 改变质点的运动状态
- 质点获得加速度

- 力矩 → 改变刚体的转动状态
- 刚体获得角加速度

力 \(F\) 对 \(z\) 轴的力矩

\[M_z(F) = F_{\tau}r = F_{\bot}h\]

- 力矩取决于力的大小、方向和作用点

- 在刚体的定轴转动中，力矩只有两个指向 (+-)

--- PAGE 015 ---
力矩并不局限于定轴转动,在一般情况下,力矩是空间矢量。力也是空间矢量。

(1) 力对点的力矩

\[\vec{M}_o = \vec{r} \times \vec{F}\]

(2) 力对定轴力矩的矢量形式

\[\vec{M}_z = \vec{r} \times \vec{F}_\perp\]

力矩的方向由右螺旋法则确定

(3) 力对任意点的力矩,在通过该点的任一轴上的投影,等于该力对该轴的力矩

\[\vec{F}_z = \vec{F}_0 \cos \alpha\]

\[\vec{M}_z = \vec{M}_0 \cos \alpha\]

--- PAGE 016 ---
1. 力矩求和只能对同一参考点(或轴)进行

\[
\vec{M}_O = \vec{M}_{10} + \vec{M}_{20} + \cdots \quad \text{矢量和}
\]

\[
M_z = M_{1z} + M_{2z} + \cdots \quad \text{代数和}
\]

2. 一个刚体所受合外力为0与所受合力矩为0是不等价的

\[
\sum \vec{F} = 0 \\
\sum \vec{M} \neq 0
\]

3. 刚体的合内力矩为0

\[
\sum \vec{M}_{i内} = 0
\]

--- PAGE 017 ---
**例** 已知棒长 \(L\),质量 \(M\),在摩擦系数为 \(\mu\) 的桌面转动(如图)

**求** 摩擦力对y轴的力矩

解 \(dm = \frac{M}{L} dx\) \(df = \mu dm \cdot g\)

根据力矩 \(dM' = -\mu \frac{M}{L} \cdot gxdx\)

\[M' = \int^{L}_{0} - \mu \frac{M}{L} \cdot gxdx = -\frac{1}{2} \mu MgL\]

- 在定轴转动中,力矩可用代数值进行计算
例如

\[\sum M_i = TR - T'r\]

--- PAGE 018 ---
## 二. 刚体对定轴的转动定律

实验证明

当 \(M\) 为零时, 则刚体保持静止或匀速转动

当存在 \(M\) 时, \(\beta\) 与 \(M\) 成正比, 此外还与刚体的质量大小及其质量分布都有关

理论推证

\[\mathcal{F}_i + \mathcal{f}_i = \Delta m_i\vec{a}_i\]

\[\vec{r}_i \times \vec{f}_i + \vec{r}_i \times \vec{F}_i = \Delta m_i\vec{r}_i \times \vec{a}_i\]

\[\sum \vec{r}_i \times \vec{f}_i + \sum \vec{r}_i \times \vec{F}_i = \sum \Delta m_i\vec{r}_i \times \vec{a}_i\]

\[\overrightarrow{M}_z = \sum \vec{r}_i \times \vec{F}_i\]

--- PAGE 019 ---
加速度: \(\vec{a}_i = \vec{a}_{i\tau} + \vec{a}_{in}\)

\[\vec{M}_z = \sum \Delta m_i\vec{r}_i \times \vec{a}_{i\tau} + \sum \Delta m_i\vec{r}_i \times \vec{a}_{in}\]

其中: \(\vec{r}_i \times \vec{a}_{in} = 0 \quad \vec{r}_i \times \vec{a}_{i\tau} = \sin(\pi/2)r_i a_{i\tau} \quad \vec{k} = r_i^2 \beta \vec{k}\)

\[M_z = (\sum \Delta m_i r_i^2) \beta\]

如果定义一个既包含物体的质量大小又反映其质量分布的物理量J, 它与M成正比

\[M \propto J\beta\]

对比牛顿第二定律 \(F=ma\), \(m\) 是描述物体惯性的物理量
J也是描述物体惯性的物理量, 并且是描述物体转动时的惯性, 称为转动惯量。单位: kg·m²

--- PAGE 020 ---
## 刚体的转动定律

\[ M_z = J\beta \]

作用在刚体上所有的外力对定轴 z 轴的力矩的代数和 = 刚体对 z 轴的转动惯量 × 角加速度

### 讨论

(1) M 正比于 β, 力矩越大, 刚体的 β 越大

(2) 力矩相同, 若转动惯量不同, 产生的角加速度不同

(3) 与牛顿定律比较: M → F, J → m, β → a

比较

\[ \vec{F} = m \vec{a} \]
\[ M_z = J \beta \]

m 是物体平动惯性的量度
J 是物体转动惯性的量度
F 改变物体平动状态的原因
M_z 改变物体绕轴转动状态的原因

--- PAGE 021 ---
# 三. 转动惯量的计算

\[J = \sum \Delta m_i r_i^2 \quad \text{质量不连续分布}\]

\[J = \int r^2 dm \quad \text{质量连续分布}\]

计算转动惯量的三个要素：(1) 总质量 (2) 质量分布 (3) 转轴的位置

求转动惯量需要用积分的方法，是本课程重点内容之一。

\[J = \int r^2 dm\]

| \(dm=\) | ρdV σdS (λdl) | 体分布 面分布 线分布 |
|---|---|---|

--- PAGE 022 ---
对于质量相同的刚体，一个质量分布靠近转轴，另一个质量分布远离转轴，从定义中可以看出，前者的转动惯量比后者小。

转动惯量仅取决于刚体本身的性质，即与刚体的质量、质量分布以及转轴的位置有关。

--- PAGE 023 ---
# 书中例题6.1(P.198)

(1) \(J\) 与刚体的总质量有关

例如两根等长的细木棒和细铁棒绕端点轴转动惯量

\[J = \int_{0}^{l} x^2 \lambda dx = \int_{0}^{l} x^2 \frac{M}{L} dx = \frac{1}{3} ML^2\]

\[J_{\text{铁}} > J_{\text{木}}\]

(2) \(J\) 与转轴的位置有关

\[J = \int_{-L/2}^{L/2} x^2 \lambda dx = \frac{1}{12} ML^2\]

同一根杆，绕端点的转动惯量是绕中点的转动惯量的4倍。

(平行轴定理，在后面)

--- PAGE 024 ---
(3) \(J\) 与质量分布有关

例如圆环绕中心轴旋转的转动惯量

\[J = \int_{0}^{L} R^2 dm = \int_{0}^{2\pi R} R^2 \lambda dl = R^2 \lambda \int_{0}^{2\pi R} dl = 2\pi R^3 \frac{m}{2\pi R} = mR^2\]

例如圆盘绕中心轴旋转的转动惯量

\[dm = \sigma ds = \frac{m}{\pi R^2} 2\pi rdr = \frac{2mr}{R^2} dr\]

\[J = \int_{0}^{m} r^2 dm = \int_{0}^{R} \frac{2m}{R^2} r^3 dr = \frac{m}{2} R^2\]

如果厚度为 \(h\) 的圆柱，质量为 \(m\) 均匀分布呢？

--- PAGE 025 ---
如果是空芯圆柱或圆环质量为m均匀分布,内外半径分别为 \(R_1\) 和 \(R_2\), 厚度为 \(h\), 求绕其中心轴旋转的转动惯量

是 \(\frac{1}{2} M(R_2^2 - R_1^2)\) 吗？

如果是圆环,则积分限从\(R_1\)积到\(R_2\):

\[J = \int_V r^2 dm = \int_{R_1}^{R_2} r^2 \rho 2 \pi r h dr = 2 \pi \rho h \int_{R_1}^{R_2} r^3 dr\]

这时的密度应为:

\[\rho = \frac{M}{\pi (R_2^2 - R_1^2)h}\]

\[J = 2 \pi \rho h \frac{1}{4} r^4 \Big|_{R_1}^{R_2} = \frac{1}{2} \pi \frac{M}{\pi (R_2^2 - R_1^2)h} h(R_2^4 - R_1^4) = \frac{1}{2} M (R_2^2 + R_1^2)\]

相同质量和体积下空心物体比实心物体的转动惯量大

--- PAGE 026 ---
# 四. 平行轴定理及垂直轴定理

1. 平行轴定理

若有两个轴互相平行，其中一个轴过质心，则：

\[ J_z' = J_z + ML^2 \]

\[ J_z' : \text{刚体绕任意轴的转动惯量} \]

\[ J_z : \text{刚体绕通过质心的轴} \]

\(L\): 两轴间垂直距离

例 已知书中例题6.1求了杆通过中心轴的转动惯量，用平行轴定理，求均匀细棒一端点的转动惯量

\[ J'_z = J_z + M \cdot \left(\frac{L}{2}\right)^2 = \frac{1}{3} ML^2 \]

\[ J_z = \frac{1}{12} ML^2 \]

--- PAGE 027 ---
**例：**过圆盘边缘与圆盘中心轴平行的轴的转动惯量。

圆盘对其中心轴的转动惯量为：MR²/2
两轴之间的距离为R，根据平行轴定理：

\[I = I_c + md^2 = \frac{1}{2} mR^2 + mR^2 = \frac{3}{2} mR^2\]

说明：

1, 这种情况用直接积分比较困难。

2, 注意不同教材中的表示符号有所差异, 此处用的是按照教材则为!

--- PAGE 028 ---
## 2. (薄板)垂直轴定理

对于无穷薄的薄板,建立坐标轴 oxyz,其中 oxy 平面在薄板平面内, \(\mathbf{z}\) 轴与薄板垂直。

\[J_z = J_x + J_y\]

例如求对圆盘的一条直径的转动惯量
已知 \(J_z = \frac{1}{2} mR^2\)
\(J_x = J_y\) \(J_x = J_y = -\frac{1}{4} mR^2\)

说明:

1, 薄板;

2, \(x, y\) 轴在薄板内, \(x, y, z\) 轴两两垂直;
3, 通常原点位于刚体的质心, 否则用平行轴定理变换。

--- PAGE 029 ---
# 例题: (重点)

半径为R, 长为L, 质量为M的实心圆柱体对中心直径的转动惯量。

解: 从圆柱上切下一个薄圆片dM, 它对x轴的转动惯量为:

\[dJ_x = dMR^2/2\]

用垂直轴定理, 得出它对z'轴的转动惯量为:

\[dJ_z' = dMR^2/4 \quad \text{其中} dM = M/Ldx\]

用平行轴定理, 得出它对z轴的转动惯量为:

\[dJ_z'' = dMR^2/4 + dMx^2\]

从-L/2到+L/2积分得

\[J = \int_{-\frac{L}{2}}^{\frac{L}{2}} \frac{1}{4} RdM + \frac{M}{L}x^2 dx = \frac{1}{4} MR^2 + \frac{1}{12} ML^2\]

--- PAGE 030 ---
\[I_{cm} = \frac{1}{12} M(3R^2 + L^2)\]

两个极限检验（物理直觉）：

1. 细长圆柱：\(L \gg R\) \(I \approx \frac{1}{12} ML^2\) (细杆绕中心的转动惯量)

2. 薄圆盘：\(L \to 0\) \(I = \frac{1}{4} MR^2\) (圆盘直径转动惯量)

圆柱对中心直径的转动惯量 = 圆盘直径惯量 + 杆的惯量

--- PAGE 031 ---
课后思考或查阅 实心均匀球体和均匀球壳的转动惯量如何导出？

--- PAGE 032 ---
思考题:

在质量为M,半径为R的匀质圆盘上挖
出半径为r的两个圆孔。圆孔中心在圆
盘半径的中点。求剩余部分对大圆盘中
心且与盘面垂直的轴线的转动惯量。

--- PAGE 033 ---
## 五.转动定律的应用举例

运用转动定律解决刚体绕定轴转动问题是本课程的重点：

1. 已知转动状态求刚体所受的力矩或力；

2. 已知所受的力或力矩求转动状态（角加速度、角速度、角位移或者转动时间）

解题要点：

1. 不仅做受力分析，更要正确分析力矩

2. 将牛顿第二定律的解题技巧类比运用于转动定律

3. 正确计算刚体转动惯量（典型结构需要记忆，复杂结构由典型结构导出）

4. 注意角量与线量的换算关系

5. 抓住刚体与刚体间、刚体与质点间运动的传递关系，力和力矩的传递关系

--- PAGE 034 ---
书中例题6.3(P202) 已知：滑轮半径为R,原量为M,绳子不可伸缩的轻绳,绳子与滑轮间无滑动,轴处无摩擦,两个悬挂物的质量分别为m1, m2。求：两重物的加速度,滑轮的角加速度,绳中的张力。

过去讨论滑轮时没有考虑滑轮质量,滑轮两端的绳子受力大小相等方向相反
这个问题中需要考虑滑轮质量,两端绳子受力是不等的。

\[T_1'R - T_2'R = J_0\beta\]

\[T_2 - m_2g = m_2a\]

\[T_1 - m_1g = -m_1a\]

\[R\beta = a\]

\[J_0 = \frac{1}{2}M R^2 \quad T_1 = T_1' \quad T_2 = T_2'\]

--- PAGE 035 ---
解方程得：

\[ \beta = \frac{1}{R} \frac{m_1 - m_2}{m_1 + m_2 + \frac{1}{2} M} g \]

\[ T_1 = \frac{2m_1m_2 + \frac{1}{2}Mm_1}{m_1 + m_2 + \frac{1}{2}M} g \]

\[ a = \frac{m_1 - m_2}{m_1 + m_2 + 1}{2g} \]

\[ T_2 = \frac{2m_1m_2 +\frac{1}{2}Mm_2}{m_1 + m_2 + 1} g \]

中学见过这类问题很多，但滑轮都是轻滑轮，不考虑滑轮的质量，\(M=0\)，将其代入上面的方程得：

\[ a = \frac{m_1}{m_1 + m_2} g \]

\[ T_1 = T_2 = \frac{2m_1m_2}{m_1+m_2} g \]

--- PAGE 036 ---
﻿书中例题6.4 (P202) 已知：两个皮带轮半径分别为\(R_1\), \(R_2\), 质量分别为\(m_1\), \(m_2\), 分别绕固定轴\(O_1\), \(O_2\)转动, 用皮带相连, 轮1作用力矩\(M_1\), 轮2有**负载力矩**\(M_2\), 皮带与轮无滑动, 轴处无摩擦。 

求：轮1的角加速度。 

解：隔离物体法分析力： 

\[J = \gamma_s MR^2 \\ M = J\beta\]

\(M\)定为正方向后, 力矩的方向与\(M\)一致则为"正"反之为"负"。
两个轮是牵连在一起运动的, 所以存在着牵连关系。 

皮带与轮没有相对滑动, 则: \(\omega_1 R_1 = \omega_2 R_2\) 

\(\beta_1 R_1 = \beta_2 R_2\) 

不计皮带质量, 则 \(T_1 = T_1', \quad T_2 = T_2'\) 

解方程组得 \(\beta_1 = \frac{2(R_2 M_1 - R_1 M_2)}{(m_1 + m_2) R_1^2 R_2}\)

--- PAGE 037 ---
﻿书中例题6.5 (P202) 已知：飞轮齿轮1绕转轴1的转动惯量\(J_1 = 98.0\) kgm\(^2\)，飞轮齿轮2绕转轴2的转动惯量\(J_2 = 78.4\text{kgm}^2\)，两齿轮咬合传动，齿数比\(Z_1:Z_2 = 3:2\)，\(r_1 = 10\text{cm}\)，轴1从静止在10s匀加速到1500r/min，求：加在轴1上的力矩M和齿轮间的相互作用力\(Q\)。 

解：飞轮1和2的动力学方程分别为
\[M_z - Qr_1 = J_1\beta_1\]
\[Qr_2 = J_2\beta_2\] 

根据齿轮传动的特点，可得 

\[\frac{r_1}{r_2} = \frac{Z_1}{Z_2} \quad \beta_2 = \frac{Z_1}{Z_2} \beta_1\]

\[M_z = [J_1 + (\frac{Z_1}{Z_2})^2]J_2\beta_1\]

\[Q = \frac{J_2}{r_1} (\frac{Z_1}{Z_2})^2 \beta_1\]

\[\beta_1 = \left(\frac{1500}{60}\right) \times 2\pi \times \frac{1}{10} = 5\pi(s^{-2})\]

\[M = \left(98.0 + 78.4 \times \frac{9}{4}\right) \times 5\pi = 4.31 \times 10^3 (N \cdot m)\]

\[Q = \left(\frac{78.4}{0.1}\right) \times \left(\frac{9}{4}\right) \times 5\pi = 27.7 \times 10^3 (N)\]

--- PAGE 038 ---
﻿例 一根长为l,质量为m的均匀细直棒,可绕轴O在竖直平面内转动,初始时它在水平位置 

求它由此下摆θ角时的ω 

解 取一质元 

\[
M = mgx_C
\]

\[
M = mgx_C
\]

\[
M = \frac{1}{2} mgl \cos \theta
\]

前面结论：\(J = 1/3 ml^2\) 

重力对整个棒的合力矩等于重力全部集中于质心所产生的力矩 

\[
\beta = \frac{M}{J} = \frac{1}{2} mgl \cos \theta \quad \frac{3}{ml^2} = \frac{3g \cos \theta}{2l} = \frac{d\omega}{dt} = \omega \frac{d\omega}{d\theta}
\]

\[
\int_{0}^{\omega} \omega d\omega = \int_{0}^{\omega} \frac{3 g \cos \theta}{2 l} d\theta \quad \Rightarrow \quad \omega = \sqrt{\frac{3 g \sin \theta}{l}}
\]

--- PAGE 039 ---
﻿例 圆盘以 ω₀ 在桌面上转动, 受摩擦力而静止 

求 到圆盘静止所需时间 

解 取一质元 \(dm = \sigma ds = \sigma \cdot 2\pi rdr\) 

\[dM = rdf = r \cdot \mu gdm\]

摩擦力矩 

\[M = \int_0^R dM = \frac{2}{3} \mu mgR\]

由转动定律 \(M = -J \frac{d\omega}{dt}\) 
\(\frac{2}{3}\mu mgR = -\frac{1}{2}mR^2\frac{d\omega}{dt}\) 

(阻碍运动的力矩 \(\rightarrow\) 加速度必为负) 

\[\int_{0}^{t} dt = -\int_{\omega_{0}}^{0} \frac{3R}{4\mu g} d\omega\] \[t = \frac{3R \omega_{0}}{4\mu g}\]

\[M = J\beta\]

--- PAGE 040 ---
﻿## 课堂练习 

1. 轮圈半径为R, 其质量M均匀分布在轮缘上, 长为R、质量为m的均质辐条固定在轮心和轮缘间, 辐条共有2 N根。今若将辐条数减少N根, 但保持轮对通过轮心、垂直于轮平面轴的转动惯量不变, 则轮圈的质量应 

(A) 不变

减少为 

\[ \frac{N}{12} m + M \]

\[ \frac{N}{6} m + M \]

\[ \begin{array}{c} \frac{N}{12} m + M \\ \frac{N}{3} m + M \end{array} 3) \]

(C) 增加为

增加为 

2. 一半径为R质量为m的均质圆形平板在粗糙的水平桌面上, 绕通过圆心且垂直于平板的OO'轴转动, 摩擦力在圆盘边沿产生的切向加速度为 

(A) 

4 

(C) 

3 

μg 

(C) 

g 

2µ 

(B) 

μg 

μgR 

2 

(E) 

μgR 

3 

μgR 

(F)

--- PAGE 041 ---
﻿### 6.3 绕定轴转动刚体的动能定理 

## 一. 转动动能 设系统包括有 \(N\) 个质量元 

\[ 
\left\{
\begin{aligned}
&\Delta m_1, \Delta m_2, \ldots, \Delta m_i, \ldots, \Delta m_N \\
&\vec{r}_1, \vec{r}_2, \ldots, \vec{r}_i, \ldots, \vec{r}_N \\
&v_1, \vec{v}_2, \ldots, \vec{v}_i, \ldots, \vec{v}_N
\end{aligned}
\right. 
\]

取 \(\Delta m_i\), 其动能为 

\[ E_{ki} = \frac{1}{2} \Delta m_i v_i^2 = \frac{1}{2} \Delta m_i r_i^2 \omega^2 \]

各质量元速度不同，但角速度相同 

刚体的总动能 

\[ E_k = \sum E_{ki} = \sum\frac{1}{2}\Delta m_i r_i^2\omega^2 = \frac{1}{2}\left(\sum \Delta m_i r_i^2\right)\omega^2 = \frac{1}{2} J\omega^2 \]

**结论** 绕定轴转动刚体的动能等于刚体对转轴的转动惯量与其角速度平方乘积的一半

--- PAGE 042 ---
﻿二. 力矩的功 

力的累积过程——力矩的空间累积效应 

- 功的定义 

\[ dA = \vec{F} \cdot d\vec{r} = \vec{F} \cos\theta ds \]

\[ = \vec{F} \cos \theta d\theta \]

\[ = \vec{F}_{\tau} r d\theta \]

\[ = M d\theta \]

力矩作功的微分形式 

- 对一有限过程 

\[ A = \int_{\theta_1}^{\theta_2} M d\theta \quad (\text{积分形式}) \quad \text{若 } M = C \quad A = M(\theta_2 - \theta_1) \]

--- PAGE 043 ---
﻿讨论 

(1) 合力矩的功 

\[A = \int_{\theta_1}^{\theta_2} \sum_i M_i d\theta = \sum_i \int_{\theta_1}^{\theta_2} M_i d\theta = \sum_i A_i\]

(2) 力矩的功就是力的功。力矩引起的转动空间积累效果和力引起的空间位移积累效果是等价的。功作为能量转换的量在任何物理过程中总是等价的。 

\[dA = \vec{F} \cdot d\vec{r} = M d\theta\]

(3) 内力矩作功之和为零(因为刚体中各质点角位移总相等)。 

\[P = \frac{dA}{dt} = \frac{M d\phi}{dt} = M\omega\]

--- PAGE 044 ---
﻿书上例题6.6 

长为l质量分布不均匀的细杆，其线密度为
\(λ = a + br\) (a、b为常量)，该杆可绕A端的
\(z\)轴在铅锤面内转动，如图所示。现将杆从
水平位置(θ=π/2) 释放，求杆转到铅锤
位置(θ=0) 过程中，重力做的功。 

解：距离转轴r处取线元dr，线元质量为
\(dm = λdr\)。当杆在任意位置θ时，该质元
的重力对z轴的力矩为 \(dM_z = -(\lambda dr)gr \sin \theta\) 

所以，杆的重力对 \(M_z = -\int_0^l (\lambda dr)gr \sin \theta = g \sin \theta \int_0^l (a + br)rdr\)
z轴的总力矩为 

\[
= -gl^2 \left( \frac{a}{2} + \frac{b}{3} l \right) \sin \theta
\]

\[
dA = M_z d\theta = -gl^2 \left( \frac{a}{2} + \frac{b}{\phantom{2}} l \right) \sin \theta d\theta
\]

\[
A = \int_{\pi/2}^{0} -gl^2 \left( \frac{a}{2} + \frac{b}{3} I \right) \sin \theta d\theta = gl^2 \left( \frac{a}{2} + \frac{b}{3} -\frac{l}{3} \right)
\]

--- PAGE 045 ---
﻿## 三. 转动动能定理 —— 力矩功的效果 

\[dA = M d\theta = (J \frac{d\omega}{dt}) d\theta = J \omega d\theta = d\left(\frac{1}{2} J \omega^2\right)\]

对于一有限过程 

\[A = \int_{\theta_1}^{\theta_2} dA = \int_{\omega_1}^{\omega_2} d\left(\frac{1}{2} J \omega^2\right) = \frac{1}{2} J \omega_2^2 - \frac{1}{2} J \omega_1^2 = \Delta E_k\]

绕定轴转动刚体在任一过程中动能的增量, 等于在该过程中作用在刚体上所有外力所作功的总和。这就是绕定轴转动刚体的——动能定理

--- PAGE 046 ---
﻿·刚体的机械能 

刚体重力势能 

\[E = E_k + E_p\]

\[E_p = \sum \Delta m_i gh_i\]

\[= \text{mg} \sum \frac{\Delta m_i h_i}{m} = \text{mgh}_c\]

\[\frac{h_c}{E_p} = 0\]

\(h_i\) 

刚体的机械能 

质心的势能 

\[E = \frac{1}{2} J\omega^2 + \text{mgh}_c\]

·刚体的机械能守恒 

对于包括刚体的系统，功能原理和机械能守恒定律仍成立 

\[条件: A_{合外力}+A_{非保内}+A_{合外力矩}=0\]

--- PAGE 047 ---
﻿书中例题6.8, P209 圆盘滑轮质量M, 半径R, 绕轻绳, 绳的另一端系一质量m的物体, 轴无摩擦, 开始时系统静止。
求: 物体下降s时, 滑轮的角速度和角加速度。 

解: 轴无摩擦, 系统机械能守恒 

m动能 m势能 M动能 
初: 0 
终: mv²/2 mgs 0 0 Jzω²/2 

牵连关系: \(v = \omega R\), \(J_z = 1/2 MR^2\) 

\[mgs = mv^2 / 2 + J_z\omega^2 / 2 = mR^2\omega^2 / 2 + MR^2\omega^2 / 4\]

\[\omega = \frac{2}{R} \sqrt{\frac{mgs}{2m + M}}\]

--- PAGE 048 ---
﻿求角加速度： 

\[
\beta = \frac{d\omega}{dt} = \frac{d}{dt} \left( \frac{2}{R} \sqrt{\frac{mgs}{2m+M}} \right) = \frac{2}{R} \sqrt{\frac{mg}{2m+M}} \frac{d}{dt} \sqrt{s}
\]

\[
= \frac{2}{R} \sqrt{\frac{mg}{2m+M}} \cdot \frac{1}{2} \frac{1}{\sqrt{s}} \frac{ds}{dt} = \frac{1}{R} \sqrt{\frac{mg}{2m+M}} \frac{1}{\sqrt{s}} \omega R
\]

其中 \(ds/dt = v = \omega R\)，并将 \(\omega\) 值代入得： 

\[
\beta = \sqrt{\frac{mg}{2m+M}} \frac{2}{R} \sqrt{\frac{mgs}{2m+M}} \frac{1}{\sqrt{s}} = \frac{2mg}{R(2m+M)}
\]

以上用刚体运动学的方法由角速度求导求角加速度，
思考：如何由动力学方法求角加速度 转动定律 

\[
TR = \frac{MR^2}{2} \beta
\]

\[
mg - T = ma
\]

\[
a = R \beta
\]

--- PAGE 049 ---
﻿# 书中习题6.13 (p227) (重点) 

以力F将一块粗糙平面均匀压在轮上，平面与轮之间的滑动摩擦系数为μ，轮为匀质圆盘，半径为R,质量为M，轴处摩擦力不计，轮的初角速度为ω₀,
问：轮转过多少度时即停止转动。 

解：盘面单位面积上的压力为 \(\frac{F}{\pi R^2}\)，以轮心为中心，以r为半径，取宽为dr的环，则环上压力为 \(dF = \frac{F}{\pi R^2} \cdot 2\pi r \cdot dr\)

环上的摩擦力为 \(df = \mu dF = \mu \frac{F}{\pi R^2} \cdot 2\pi r \cdot dr = \mu \frac{F}{R^2} \cdot 2rdr\)

\(df\)对轴的力矩为 \(dM = \mu \frac{F}{R^2} \cdot 2r^2 dr\) 

\[ \text{整个圆盘受到的摩擦力矩为} \quad M = \int_0^R \mu \frac{F}{R^2} \cdot 2r^2 dr = \frac{2}{3} \mu FR \]

\[ \text{由动能定理, 有} \quad -M\varphi = 0 - J\omega^2 / 2 \]

\[ \varphi = \frac{3mR\omega_0^2}{8\mu F} \]

--- PAGE 050 ---
﻿## 6.4 动量矩和动量矩守恒定律 

## 一. 回顾：质点动量矩（角动量） 

\[ \vec{L}_o = \vec{r} \times \vec{P} = \vec{r} \times m\vec{v} \]

其大小 

\[ \boldsymbol{L}_o =r p \sin \varphi = m r v \sin \varphi \]

惯性参照系 

特例：质点作圆周运动 \(L = rp = mr\vec{v}\)

--- PAGE 051 ---
﻿## 二. 刚体定轴转动的动量矩定理和动量矩守恒定律 

1. 刚体定轴转动的动量矩 

刚体上任一质点对 Z 轴的动量矩都具有相同的方向 

\[L_z = \sum_i \Delta m_i v_i r_i = \sum_i \Delta m_i r_i^2 \omega = J_z \omega\]

\[L_z = J_z \omega \quad \text{(所有质元的动量矩之和)}\]

2. 刚体定轴转动的动量矩定理 

\[\text{由转动定律} \quad M_z = J \frac{d\omega}{dt} \quad \text{动量矩定理}\] \[\quad M_z dt = J d\omega = d(J\omega) \quad \text{微分形式}\] 

\[\int_{t_1}^{t_2} M_z dt = \int_{\omega_1}^{\omega_2} d(J\omega) = J\omega_2 - J\omega_1 \quad (\text{动量矩定理积分形式})\]

定轴转动刚体所受合外力矩的冲量矩等于其动量矩的增量

--- PAGE 052 ---
﻿冲量 \(\vec{I} = \vec{F} t\) 

冲量矩 \(\vec{M}_1 = \vec{r} \times \vec{F} t = \vec{r} \times \vec{I}\) 

书中例题6.13(p.217) 

长l, 质量M, 铅直悬挂, 初始处于静止状态, 杆的中心受一冲量I作用, 方向与杆垂直。 

求: 冲量作用结束时, 杆的角速度。 

解: 冲量对转轴的冲量矩为 \(\frac{l}{2}I\) 

根据动量矩定理: \( J_z \omega = \frac{l}{2}I \) 其中, \( J_z = \frac{1}{3}Ml^2 \) 

\[ \omega = \frac{3I}{2Ml} \]

--- PAGE 053 ---
﻿3. 刚体定轴转动的动量矩守恒定律 

对定轴转动刚体 

\[M_z = 0\]

\[L = J\omega = C\]

**注：1)** 守恒条件为 \(\vec{M}_{\text{外}} = 0\) 

或 \(M_{\text{轴}} = 0\) 不是 \(\int \vec{M}_{\text{外}} dt = 0\) 

**向量守恒定律彼此独立** 

\[当 \vec{F}_{\text{外}} = 0 \text{时}, \vec{p} = \text{恒矢量}\] \[当 \vec{M}_{\text{外}} = 0 \text{时}, \vec{L} = \text{恒矢量}\]

**3）运用动量矩定理和动量矩守恒定理时，应在将系统中的所有质点和刚体的运动物理量变换到同一惯性参照系下使用。**

--- PAGE 054 ---
﻿动量矩守恒定律适用情形举例说明 

(1) 对于系统： 

\(J_i、\vec{\omega}_i\) 均可以变化,
但 \(\sum J_i\vec{\omega}_i\) 不变 

对质点、刚体、形变体及其它们组成的
系统均适用, 对一切宏观、微观物体的
转动问题均适用。 

(2) 对于变形体: \(J, \vec{\omega}\) 均可以变化, 但 \(J\vec{\omega}\) 不变

--- PAGE 055 ---
﻿(图片页 - 动量矩守恒定律图示)

--- PAGE 056 ---
﻿书中例题6.15(p.220) 

半径为 \(R\), 质量为 \(4m\) 且均匀分布的转盘可绕铅垂轴无摩擦地转动, 盘上站有质量为 \(m\) 的四个人, 两个人站在盘的边沿, 两个人站在 \(R/2\) 处, 整个系统开始以角速度 \(\omega_0\) 转动。此后, 人相对于盘作圆周运动, 站在边沿上的两人相对于盘的速度为 \(\mu\), 站在 \(R/2\) 处的两人相对于盘的速度为 \(2\mu\)。求: (1) 人走动后, 转盘的角速度; (2) 要使转盘停止转动, \(\mu\) 的大小。 

解: (1) 以人和盘组成的系统对轴的外力矩为 0, 故系统对轴的动量矩守恒, 即 

\[
\frac{1}{2}(4m)R^2 + (2m)R^2 + (2m)\left(\frac{R}{2}\right)^2\omega_0 = \frac{1}{2}(4m)R^2\omega + 2mR^2\left(\frac{\mu}{R} + \omega\right) + 2m\left(\frac{R}{2}\right)^2\left(\frac{2\mu}{R/2} + \omega\right)
\]

(2) 令 \(\omega = 0\), 可求出使转盘停止转动的 \(\mu\) 的大小

\(\omega_0 - \frac{8\mu}{9R} = 0\), \(\mu = -\frac{9}{8}R\omega_0\)

动量矩定理和动量矩守恒定理适用于惯性系, 解题时应该把所有研究对象放在同一惯性系中进行研究。

--- PAGE 057 ---
﻿# 课堂练习 

1. 一个圆盘通过盘心垂直于盘面的水平轴转动, 轴承间摩擦不计。如图所示, 对射来两个质量、速率均相同、速度方向相反并在同一直线上的子弹, 它们同时入射到圆盘边并留在盘边沿处, 问子弹入射后, 圆盘和子弹组成的系统的动量矩和角速度如何变化? ( ) 

(A) 动量矩变小, 角速度变小
(B) 动量矩变大, 角速度变大
(C) 动量矩不变, 角速度变小
(D) 动量矩不变, 角速度不变

--- PAGE 058 ---
﻿书中例题6.16(p.221) 重点 

长为L, 质量为M的均匀杆, 一端悬挂, 由水平位置无初速度地下落, 在铅直位置与质量为m的物体A做完全非弹性碰撞, 碰后, 物体A沿摩擦系数为μ的水平面滑动。求: 物体A滑动的距离。 

解：整个过程分为三个阶段： 

1、杆由水平位置绕端点的轴转动：刚体机械能守恒 

2、杆与A作完全非弹性碰撞，刚体与质点组成的系统动量矩守恒，**注意不是动量守恒！**（思考为什么？） 

3、质点A滑动：动能被摩擦力耗散掉。 

第一阶段：机械能守恒 

动能 
初： 0 
终： \(1/2J_\omega\omega^2\) 

\[ \therefore 1/2J\omega^2 = MgL/2 \]

\(\therefore \omega^2 = 3g/L\) 

其中 \(J = 1/3ML^2\)

--- PAGE 059 ---
﻿第二阶段：杆和质点A组成的系统动量矩守恒
需要分别求出初、末状态杆和质点的动量矩
初：\(J_z\omega\);
终：\(J_z\omega' + mL^2\omega'\)
∴ \(J_z\omega=J_z\omega' + mL^2\omega'\) 

代入\(J_z\)和\(ω\)值，得： 

\[\frac{1}{3}ML^2\sqrt{\frac{3g}{L}}=\frac{1}{3}ML^2\omega'+mL^2\omega',\]

\[\omega' = \frac{M \sqrt{\frac{3g}{L}}}{M+3m}\]

第三阶段，动能定理
物体A的速度：\(\omega'L\); 摩擦力\(mg\mu\)做功，动能减少 

\[\frac{1}{2}m(L\omega')^2 = mg \mu s \quad \text{或} \quad s = \frac{3LM^2}{2\mu(M+3m)^2}\]

--- PAGE 060 ---
﻿例 一个刚体系统，如图所示，已知，转动惯量 

\[J = \frac{1}{3} ml^2, \text{现有一水平力作用于距轴为} l'\text{处}\]

**求** 轴对棒的作用力（也称轴反力）。 

**解** 设轴对棒的作用力为 \(N\) 

\[N_x, N_y\]

由转动定律 \(Fl'=J\beta\) 

\[\text{打击中心} \rightarrow N_x = 0\]

\[N_x = \frac{mlFl'}{2J} - F = F(\frac{3l'}{2l} - 1) \rightarrow l' = \frac{2}{3} l \rightarrow N_y = mg\]

--- PAGE 061 ---
# 区分两类冲击摆

(1)

(2)

**质点** ←→ **质点** 柔绳无切向力
➤ 水平方向：\(F_x = 0\), \(p_x\) 守恒
\[\vec{v}_0 = (m+M)\vec{v}\]
➤ 对 \(O\) 点：\(\vec{M} = 0\), \(\vec{L}\) 守恒
\[mv_0 l = (m+M)vl\]

**质点** ←→ **定轴刚体(不能简化为质点)**
轴作用力不能忽略，动量不守恒，
但对 \(O\) 轴合力矩为零，角动量守恒
\[mv_0 l = ml^2\omega + \frac{1}{3} Ml^2 \cdot \omega \quad v = \omega l\]

--- PAGE 062 ---
# 书中习题6.22 (p228)（重点）

6.22 一均质细杆, 长 \(L=1\) m, 可绕通过一端的水平光滑轴 \(O\) 在铅垂面内自由转动, 如图所示. 开始时杆处于铅垂位置, 今有一粒子弹沿水平方向以 \(v=10\) m/s 的速度射入细杆. 设入射点离 \(O\) 点的距离为 \(3L/4\), 子弹的质量为杆质量的 \(1/9\), 试求: (1) 子弹与杆开始共同运动的角速度; (2) 子弹与杆共同摆动能达到的最大角度.

解 (1) 在子弹射入细杆的过程中, 子弹与细杆组成的系统动量矩守恒, 故有

\[ \frac{1}{9} Mv \frac{3}{4} L = \left[ \frac{1}{9} M \left( \frac{3}{4} L \right)^2 + \frac{1}{3} ML^2 \right] \omega \]

解此式可得子弹与杆碰后共同运动的角速度, 即

\[ \omega = \frac{4v}{19L} = 2.10 \text{ rad/s} \]

--- PAGE 063 ---
射入后,在子弹与杆共同摆动过程中,系统机械能守恒,
设杆摆动能达到的最大角度为 θ,则有

\[
\frac{1}{2} \left( \frac{1}{9} M \left( \frac{3}{4} L \right)^2 + \frac{1}{3} ML^2 \right) \omega^2 =
\frac{1}{9} Mg \frac{3}{4} L (1 - \cos \theta) + Mg \frac{L}{2} \left( 1 - \cos \theta \right)
\]

\[
\text{解此式,得} \cos\theta = 1 - \frac{2v^2}{133Lg} = 0.8466 \
\theta = 32.16^\circ
\]

--- PAGE 064 ---
\[mva = \left(\frac{1}{3} Ml^2 + ma^2\right)\omega\]

\[ \frac{1}{2} \left( \frac{1}{3} Ml^2 + ma^2 \right) \omega^2 = mga(1-\cos30^\circ) + Mg \frac{1}{2} (1-\cos30^\circ) \]

\[ mva = \frac{1}{3} M l^2 \omega + mv' a \]

\[ \frac{1}{2} \frac{1}{3} M l^2 \omega^2 = Mg \frac{l}{2} (1-\cos30^\circ) \]

\[ mva cos\alpha = \left( \frac{1}{3} M l^2 + ma^2 \right) \omega \]

\[ \frac{1}{2} \left( \frac{5}{3} M l^2 + ma^2 \right) \omega^2 = mga \left( 1 - \cos 30^\circ \right) + Mg \frac{l}{2} \left( 1 - \cos 30^\circ \right) \]

--- PAGE 065 ---
例 一长为l的匀质细杆，可绕通过中心的固定水平轴在铅垂面内自由转动，开始时杆静止于水平位置。一质量与杆相同的昆虫以速度 \(v_0\) 垂直落到距点 \(O l/4\) 处的杆上，昆虫落下后立即向杆的端点爬行，如图所示。若要使杆以匀角速度转动

求 昆虫沿杆爬行的速度。

解 昆虫落到杆上的过程为完全非弹性
碰撞,对于昆虫和杆构成的系统,合
外力矩为零,动量矩守恒

\[ 
\begin{align*} mv_0 & = \left( \frac{1}{4}ml^2 + m\left( \frac{l}{4} \right)^2 \right) \omega \\ \omega &= \frac{12v_0}{7l} \end{align*} 
\]

--- PAGE 066 ---
转动定律

\[M_z = \frac{d(J_z\omega)}{dt}\]

杆和虫组成的系统重力矩在变，转动惯量也在变
可以类比变量牛顿第二定律问题的处理思路！

使杆以匀角速度转动

\[M_z = \omega \frac{dJ_z}{dt}\]

其中

\[M_z = mgr \cos \theta\]

\[J_z = \left(\frac{1}{12} ml^2 + mr^2\right)\]

代入得

\[mgr \cdot \cos \theta = 2m\omega r \frac{dr}{dt}\]

\[\nu = \frac{dr}{dt} = \frac{g \cos \theta}{2\omega} = \frac{g}{2\omega} \cos \omega t = \frac{7\frac{1}{2}g}{24\nu_0} \cos\left(\frac{12}{7}\nu_0 t\right)\]

--- PAGE 067 ---
## 四. 进动

高速自转的陀螺在陀螺重力对支点O 的力矩作用下发生进动
陀螺的动量矩近似为

\[ \vec{L} = J \vec{\omega} \]

**动量矩定理**

\[ \vec{M} = \frac{d \vec{L}}{dt} \rightarrow\]

\[ d\vec{L} = Mdt \]

\[ d\vec{L} // \vec{M} \]

当 \(\vec{M} \perp \vec{L}\) 时

则 \(\vec{L}\) 只改变方向，不改变大小(进动)

--- PAGE 068 ---
• 进动角速度 Ω

动量矩定理 \(\vec{M} = \frac{d\vec{\Omega}}{dt}\)

而且 \(|\vec{\Omega}| = |\vec{L}\sin\theta|\Omega\)

\[|\vec{M}| = \frac{d\vec{L}}{dt} = |\vec{L}\sin\theta\frac{d\Omega}{dt}| = |\vec{L}\sin\theta \cdot \Omega|\]

所以

\[\Omega = \frac{|\vec{M}|}{|\vec{L}\sin\theta|} = \frac{|\vec{M}|}{J\omega\sin\theta} \propto \frac{1}{\omega}\]

\[\omega \uparrow \Omega \downarrow\]

以上只是近似讨论，只适用高速自转，即 \(\omega >> \Omega\)

--- PAGE 069 ---
<center>质点的运动规律和刚体定轴转动规律的对比（一）</center>

| 质点运动 | 刚体定轴转动 |
|---|---|
| 速度 \(\vec{v} = \frac{d\vec{r}}{dt}\) | 角速度 \(\omega = \frac{d\theta}{dt}\) |
| 加速度 \(\vec{a} = \frac{d\vec{v}}{dt}\) | 角加速度 α = \(\frac{d\omega}{dt}\) |
| 质量 \(m\) ，力F | 转动惯量J, 力矩M |
| 力的功 \(A = \int_{a}^{b} \vec{F} \cdot d\vec{r}\) | 力矩的功 \(A = \int_{\theta_{a}}^{\theta_{b}} M d\theta\) |
| 动能 \(E_k = \frac{1}{2} mv^2\) | 转动动能 \(E_k = \frac{1}{2} J\omega^2\) |
| 势能 \(E_p = mgh\) | 转动物能 \(E_p = mgh_c\) |

角量与线量的关系

\[s = r\theta \qquad \nu = r\omega \qquad a_\tau = r\beta \qquad a_n = r\omega^2\]

--- PAGE 070 ---
质点的运动规律和刚体定轴转动规律的对比(二)

| 质点运动 | 刚体定轴转动 |
|---|---|
| 牛顿定律 \(\vec{F} = m\vec{a}\) | 转动定律 \(\dot{\vec{M}} = J\vec{\alpha}\) |
| 动量定理 \(\int_{0}^{t} F \text{dt} = m_i \vec{v}_i - m_i \vec{v}_{i0}\) | 角动量定理 \(\int_{0}^{t} M \text{dt} = J \omega - J_0 \omega_0\) |
| 动量守恒 \(\sum_{i} m_i \vec{v}_i = \sum_{i} m_i\vec{v}_{i0}\) | 角动量守恒 \(\vec{J} \vec{\omega} = \vec{J}_0 \vec{\omega}_0\) |
| 动能定理 \(A = \frac{1}{2} mv^2 - \frac{1}{2} mv_0^2\) | 转动动能定理 \(A = \frac{1}{2} J \omega^2 - \frac{1}{2} J_0 \omega_0^2\) |
| 机械能守恒 \(E_k + E_p = \text{const}\) | 机械能守恒 \(E_k + E_p = \text{const}\) |

--- PAGE 071 ---
第三次作业（教材8个题，补充2个题，一共10个）：

P. 191 5.4; 5.6; 5.10

P. 226 6.5; 6.6; 6.17; 6.19; 6.21

9. 一质量为m、长为l的均质细杆，可绕垂直于平面、穿过O点的转轴转动，转轴距A端l/3。今使杆从静止开始由水平位置绕O点转动，求：

(1) 杆水平位置时的角加速度；

(2) 杆垂直位置时的角速度和角加速度；

(3) 垂直位置时，杆的B端与质量同为m的物块C发生完全非弹性碰撞后，粘在一起转动，求杆能向上转过的最大角度θ。

10. 一个匀质圆盘质量为m，半径为R，绕中心定轴以初角速度转动，盘各点单位面积上所受空气阻力与各点到转轴的距离成正比，即 \(f(r) = -kr\)，k为已知常数，到盘停止转动时，求：(1)所用的时间；(2)转过的角度。
