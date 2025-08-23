Name:           hugo
Version:        0.148.2
Release:        1
Summary:        The world’s fastest framework for building websites.
License:        Apache-2.0
Vendor:         Test-Only
URL:            https://gohugo.io
Source0:        https://github.com/gohugoio/hugo/archive/refs/tags/v%{version}.tar.gz
BuildArch:      x86_64
BuildRequires:  go
%global         SHA256SUM0 562024495bb23ee54d11bbb63d15156213d40b24c5f5276bc8851dc6135b8602

%description
Hugo is one of the most popular open-source static site generators.
With its amazing speed and flexibility, Hugo makes building websites fun again.

%prep
echo "%{SHA256SUM0}  %{SOURCE0}" | sha256sum -c -
%setup -q

%build
go build -ldflags="-s -w" -buildmode=pie
./hugo completion bash > hugo.bash
./hugo completion bash > hugo.zsh
./hugo completion fish > hugo.fish

%check
go test

%install
install -Dm 755 hugo %{buildroot}%{_bindir}/hugo
install -Dm 644 hugo.bash %{buildroot}%{_datadir}/bash-completion/completions/hugo
install -Dm 644 hugo.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_hugo
install -Dm 644 hugo.fish  %{buildroot}%{_datadir}/fish/vendor_completions.d/hugo.fish


%files
%{_bindir}/hugo
%{_datadir}/bash-completion/completions/hugo
%{_datadir}/zsh/site-functions/_hugo
%{_datadir}/fish/vendor_completions.d/hugo.fish
%license LICENSE
