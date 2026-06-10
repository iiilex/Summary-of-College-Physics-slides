# 第七章 机械振动

## 一、知识点总结

### 1. 机械振动基本概念
- **机械振动**：物体在一定位置附近作来回往复的运动。
- **广义振动**：任一物理量（位移、电流等）在某一数值附近反复变化。
- 振动形式：机械振动、电磁振动等。

### 2. 简谐振动（SHM）
- 物体离开平衡位置的位移 $x$ 随时间 $t$ 按余弦（或正弦）函数变化。
- **动力学特征**：所受合力的方向与位移方向相反，大小与位移成正比。
- **运动学特征**：位移满足二阶常系数线性齐次微分方程。
- **特点**：等幅振动、周期振动。
- **判断简谐振动的三要素**（同时满足）：
  1. 受力特征 $F=-kx$；
  2. 运动微分方程形式 $\frac{d^2x}{dt^2}+\omega^2 x=0$；
  3. 运动方程形式 $x=A\cos(\omega t+\varphi)$。

### 3. 描述简谐振动的特征量
- **振幅 $A$**：最大位移的绝对值（参考圆的半径），由初始条件决定。
- **周期 $T$**：完成一次全振动所需的时间。
- **频率 $\nu$**：单位时间内完成全振动的次数。
- **角频率（圆频率）$\omega$**：旋转矢量的角速度。
- **相位 $\omega t+\varphi$**：决定振动物体在任一时刻的位置和运动状态。
- **初相 $\varphi$**：$t=0$ 时的相位，由初始条件决定。
- 三者关系：$\omega=2\pi\nu=\dfrac{2\pi}{T}$。

### 4. 由初始条件确定振幅与初相
初始条件：$x_0=A\cos\varphi$，$v_0=-\omega A\sin\varphi$。
- 振幅：$A=\sqrt{x_0^2+\dfrac{v_0^2}{\omega^2}}$。
- 初相：$\tan\varphi=-\dfrac{v_0}{\omega x_0}$（$\varphi$ 在 $-\pi\sim\pi$ 之间，需由初条件判断取舍）。

### 5. 速度与加速度
- 速度：$v=\dfrac{dx}{dt}=-\omega A\sin(\omega t+\varphi)$，$v_{\max}=\omega A$。
- 加速度：$a=\dfrac{d^2x}{dt^2}=-\omega^2 A\cos(\omega t+\varphi)$，$a_{\max}=\omega^2 A$。
- 相位关系：$v$ 与 $x$ 相差 $\pi/2$，$a$ 与 $v$ 相差 $\pi/2$，$a$ 与 $x$ 相差 $\pi$。

### 6. 旋转矢量表示法
- 自原点作大小为 $A$ 的矢量，以角速度 $\omega$ 逆时针旋转。
- 初始时与 $x$ 轴夹角为 $\varphi$，$t$ 时刻与 $x$ 轴夹角为 $\omega t+\varphi$。
- 矢端在 $x$ 轴的投影即简谐振动的位移 $x=A\cos(\omega t+\varphi)$。

### 7. 弹簧振子（固有频率）
- 角频率：$\omega=\sqrt{\dfrac{k}{m}}$。
- 周期：$T=2\pi\sqrt{\dfrac{m}{k}}$。
- 频率：$\nu=\dfrac{1}{2\pi}\sqrt{\dfrac{k}{m}}$。
- 周期和频率由振动系统决定；振幅、初相由初条件决定。
- **重要结论**：重力（或任一恒力）只影响谐振子系统的平衡位置，不影响固有频率。

### 8. 单摆（小角度 $\theta<5^\circ$ 近似下为谐振动）
- 动力学方程：$\dfrac{d^2\theta}{dt^2}+\dfrac{g}{l}\theta=0$。
- 角频率：$\omega=\sqrt{\dfrac{g}{l}}$。
- 周期：$T=2\pi\sqrt{\dfrac{l}{g}}$。
- 单摆周期与摆锤质量无关；可由 $T$、$l$ 测当地重力加速度 $g$。

### 9. 复摆（物理摆，小角度近似下为谐振动）
- 角频率：$\omega=\sqrt{\dfrac{mgl}{J}}$。
- 周期：$T=2\pi\sqrt{\dfrac{J}{mgl}}$。
- $J$ 为刚体对转轴的转动惯量，可由 $T$ 测定 $J$。

### 10. 简谐振动的能量
- 动能：$E_k=\dfrac{1}{2}mv^2=\dfrac{1}{2}kA^2\sin^2(\omega t+\varphi)$。
- 势能：$E_p=\dfrac{1}{2}kx^2=\dfrac{1}{2}kA^2\cos^2(\omega t+\varphi)$。
- 总能：$E=E_k+E_p=\dfrac{1}{2}kA^2$（与振幅平方成正比且守恒）。
- 周期平均值：$\overline{E_k}=\overline{E_p}=\dfrac{1}{2}E$。

### 11. 简谐振动的合成
**（1）同方向、同频率合成**：
- 合振动仍为同频率的简谐振动 $x=A\cos(\omega t+\varphi)$。
- 振幅：$A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\varphi_2-\varphi_1)}$。
- 初相：$\tan\varphi=\dfrac{A_1\sin\varphi_1+A_2\sin\varphi_2}{A_1\cos\varphi_1+A_2\cos\varphi_2}$。
- 同相（$\Delta\varphi=2k\pi$）时 $A=A_1+A_2$ 最大；反相（$\Delta\varphi=(2k+1)\pi$）时 $A=|A_1-A_2|$ 最小。
- $\Delta\varphi>0$ 时 $x_2$ 比 $x_1$ 超前。

**（2）同方向、不同频率合成 — 拍**：
- 合振动 $x=2A\cos\left(2\pi\dfrac{\nu_2-\nu_1}{2}t\right)\cos\left(2\pi\dfrac{\nu_2+\nu_1}{2}t\right)$。
- 拍频：$\nu_{\text{拍}}=|\nu_2-\nu_1|$。
- 拍周期：$T_{\text{拍}}=\dfrac{1}{|\nu_2-\nu_1|}$。

**（3）相互垂直的同频率合成**：
- 轨迹方程：$\dfrac{x^2}{A^2}+\dfrac{y^2}{B^2}-\dfrac{2xy}{AB}\cos(\beta-\alpha)=\sin^2(\beta-\alpha)$（椭圆类）。
- 特殊情形：
  - 同相（$\beta-\alpha=0$）：$y=\dfrac{B}{A}x$（直线）；
  - 反相（$\beta-\alpha=\pi$）：$y=-\dfrac{B}{A}x$（直线）；
  - $\beta-\alpha=\dfrac{\pi}{2}$：$\dfrac{x^2}{A^2}+\dfrac{y^2}{B^2}=1$（顺时针椭圆，$A=B$ 时为圆）；
  - $\beta-\alpha=\dfrac{3\pi}{2}$：$\dfrac{x^2}{A^2}+\dfrac{y^2}{B^2}=1$（逆时针椭圆，$A=B$ 时为圆）。

**（4）相互垂直的不同频率合成**：
- 频率比为简单整数比时，轨迹为稳定的封闭曲线 — 李萨如图形，可用于测频率和相位差。

### 12. 阻尼振动
- 阻尼振动：振幅（或能量）随时间减小的振动。
- 阻尼因子：$\beta=\dfrac{\gamma}{2m}$；固有角频率：$\omega_0=\sqrt{\dfrac{k}{m}}$。
- 运动微分方程：$\dfrac{d^2x}{dt^2}+2\beta\dfrac{dx}{dt}+\omega_0^2 x=0$。
- **弱阻尼**（$\beta<\omega_0$）：$x=A_0e^{-\beta t}\cos(\omega t+\varphi)$，$\omega=\sqrt{\omega_0^2-\beta^2}$，$T=\dfrac{2\pi}{\sqrt{\omega_0^2-\beta^2}}$。
- 振幅随时间指数衰减；周期比固有周期长。
- **临界阻尼**（$\beta=\omega_0$）与 **过阻尼**（$\beta>\omega_0$）：为非周期运动，缓慢回到平衡位置。

### 13. 受迫振动与共振
- 受迫振动：系统在周期性外力持续作用下所发生的稳定振动，频率等于驱动力的频率。
- 运动微分方程：$\dfrac{d^2x}{dt^2}+2\beta\dfrac{dx}{dt}+\omega_0^2 x=h\cos\omega t$。
- 稳定后：$x=A\cos(\omega t+\varphi)$，$A=\dfrac{h}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}}$。
- **共振**：振幅达极大值的现象。
  - 共振角频率：$\omega_{\text{共}}=\sqrt{\omega_0^2-2\beta^2}$。
  - 共振振幅：$A_{\text{共}}=\dfrac{h}{2\beta\sqrt{\omega_0^2-\beta^2}}$。
  - $\beta$ 越小，$\omega_{\text{共}}$ 越接近 $\omega_0$，$A_{\text{共}}$ 越大；$\beta=0$ 时 $A_{\text{共}}\to\infty$（尖锐共振）。
- 防止共振：破坏外力周期性、改变系统固有频率、改变外力频率、增大阻尼。

---

## 二、公式汇总

- **简谐振动方程**：$x=A\cos(\omega t+\varphi)$
  说明：$A$ 振幅，$\omega$ 角频率，$\varphi$ 初相；由振动系统及初始条件决定。

- **动力学方程**：$F=-kx$
  说明：$k$ 劲度系数，$x$ 偏离平衡位置的位移；弹性恢复力与位移成正比反向。

- **运动微分方程**：$\dfrac{d^2x}{dt^2}+\omega^2 x=0$
  说明：$\omega^2=\dfrac{k}{m}$，是简谐振动的判别方程。

- **周期、频率、角频率关系**：$T=\dfrac{2\pi}{\omega}$，$\nu=\dfrac{1}{T}=\dfrac{\omega}{2\pi}$
  说明：描述振动快慢的三种等价参数。

- **弹簧振子**：$\omega=\sqrt{\dfrac{k}{m}}$，$T=2\pi\sqrt{\dfrac{m}{k}}$
  说明：$k$ 弹簧劲度系数，$m$ 振子质量；系统固有属性，与振幅无关。

- **振幅与初相**（初始条件）：$A=\sqrt{x_0^2+\dfrac{v_0^2}{\omega^2}}$，$\tan\varphi=-\dfrac{v_0}{\omega x_0}$
  说明：$x_0$、$v_0$ 为 $t=0$ 时的位移和速度。

- **速度、加速度**：$v=-\omega A\sin(\omega t+\varphi)$，$a=-\omega^2 A\cos(\omega t+\varphi)$
  说明：$v$ 比 $x$ 超前 $\pi/2$，$a$ 比 $v$ 超前 $\pi/2$（即 $a$ 与 $x$ 反相）。

- **单摆周期**：$T=2\pi\sqrt{\dfrac{l}{g}}$
  说明：$l$ 摆长，$g$ 重力加速度；仅在小角度（$\theta<5^\circ$）下成立。

- **复摆周期**：$T=2\pi\sqrt{\dfrac{J}{mgl}}$
  说明：$J$ 刚体对转轴的转动惯量，$m$ 刚体质量，$l$ 质心到转轴距离；小角度近似下成立。

- **简谐振动能量**：$E_k=\dfrac{1}{2}kA^2\sin^2(\omega t+\varphi)$，$E_p=\dfrac{1}{2}kA^2\cos^2(\omega t+\varphi)$，$E=\dfrac{1}{2}kA^2$
  说明：总能恒定且与振幅平方成正比；周期平均 $\overline{E_k}=\overline{E_p}=\dfrac{1}{4}kA^2$。

- **同方向同频率合成**：$A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\varphi_2-\varphi_1)}$，$\tan\varphi=\dfrac{A_1\sin\varphi_1+A_2\sin\varphi_2}{A_1\cos\varphi_1+A_2\cos\varphi_2}$
  说明：合振动仍为同频率简谐振动；$\Delta\varphi=2k\pi$ 同相（振幅最大），$\Delta\varphi=(2k+1)\pi$ 反相（振幅最小）。

- **拍频**：$\nu_{\text{拍}}=|\nu_2-\nu_1|$
  说明：两同方向、不同频率且频率差很小的谐振动合成时，振幅周期性变化。

- **相互垂直同频率合成轨迹**：$\dfrac{x^2}{A^2}+\dfrac{y^2}{B^2}-\dfrac{2xy}{AB}\cos(\beta-\alpha)=\sin^2(\beta-\alpha)$
  说明：$\alpha$、$\beta$ 分别为 $x$、$y$ 方向振动的初相；轨迹为椭圆类二次曲线，相位差不同形状不同。

- **阻尼振动方程**（弱阻尼 $\beta<\omega_0$）：$x=A_0 e^{-\beta t}\cos(\omega t+\varphi)$，$\omega=\sqrt{\omega_0^2-\beta^2}$
  说明：$\beta=\dfrac{\gamma}{2m}$ 为阻尼因子，$\gamma$ 为阻力系数；振幅指数衰减。

- **受迫振动振幅**：$A=\dfrac{h}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}}$
  说明：$h=H/m$ 为驱动力幅除以质量，$\omega$ 为驱动力角频率；稳态振幅。

- **共振条件**：$\omega_{\text{共}}=\sqrt{\omega_0^2-2\beta^2}$，$A_{\text{共}}=\dfrac{h}{2\beta\sqrt{\omega_0^2-\beta^2}}$
  说明：驱动力的角频率等于共振频率时，振幅达极大值。
