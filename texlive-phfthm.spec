Name:		texlive-phfthm
Version:	60735
Release:	2
Summary:	Goodies for theorems and proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfthm
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfthm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfthm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfthm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides enhanced theorem and proof environments
based on the amsthm original versions. It allows for hooks to
be placed, adds some default goodies and is highly
customizable. In particular, it can connect theorems to proofs,
automatically producing text such as "See proof on page XYZ"
and "Proof of Theorem 4: ...".

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfthm
%{_texmfdistdir}/tex/latex/phfthm
%doc %{_texmfdistdir}/doc/latex/phfthm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
