Name:           lxgw-wenkai
Version:        1.520
Release:        1
Summary:        一款开源中文字体，基于 FONTWORKS 出品字体 Klee One 衍生
License:        OFL-1.1
Vendor:         Test-Only
URL:            https://lxgw.github.io
Source0:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/lxgw-wenkai-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fontpackages-devel
%global         SHA256SUM0 f069bccc54392186ae48f676ecc73964b71f28ef740b6e75231a90946fe396b1
%reconfigure_fonts_prereq

%description
2020 年 12 月，日本著名字体厂商 FONTWORKS 在 GitHub 上发布了 7 款日文字体，分别为 Train、Klee、Stick、Rock-n-Roll、Reggae、Rampart 和 DotGothic16，根据 SIL Open Font License 1.1 授权许可开源。7 款开源日文字体各有各的特点，而这 7 款字体中，字符数量最多的是 Klee。
这是一款有着日本教科书体风格的字体，兼有仿宋和楷体的特点。一些 DIY 字体爱好者曾先后用仿宋等字体补全这款字体，作为手机系统的美化字体移植在 iOS、Android 等手机系统中，受到很多玩机发烧友的欢迎。不过这样补全的字体有一些不足之处。 第一，原有字体和后补字体之间有着一定的差异，致使一些不同的文字（如 Klee 原有汉字与后补简体字）混排之后会有一定的违和感。 第二，由于补字所用的字体为商业版权字体，补全之后不可用于商业用途，还会有侵权的风险。此外，目前现有的开源中文字库里，楷体类寥寥无几，仿宋类则几乎没有。
鉴于此，也为了丰富开源中文字体中的楷体门类，2021 年 1 月 20 日起，本人开始了为 Klee One 这一高质量的日文开源字体补全简繁常用字的尝试。因该字体具有一定的「文艺气息」，命名 「霞鹜文楷」（其实当初是感觉这款字体适合正文阅读定名「文楷」，后来发现这款字体可能并不太适合大段正文排版，相比之下更加适合诗词之类的中等长度文本排版，或者注释排版）。由于 Klee One 字体的 Regular 字重太细不太适合阅读，选取原字体 SemiBold 字重作为 Regular 字重。经过长时间的积累，目前已发展成简繁日韩均支持的 3 字重字体家族。

%prep
echo "%{SHA256SUM0}  %{SOURCE0}" | sha256sum -c -
%setup -q -n "lxgw-wenkai-v%{version}"

%build

%install
install -d %{buildroot}%{_fontsdir}/%{name}/
install -m 644 *.ttf %{buildroot}%{_fontsdir}/%{name}/

%files
%{_fontsdir}/%{name}/
%license OFL.txt

# 安装或卸载此软件包后调用 fonts-config
%reconfigure_fonts_scriptlets
