Name:		texlive-fixpdfmag
Version:	15878
Release:	1
Summary:	Fix magnification in PDFTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/misc/fixpdfmag.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixpdfmag.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A recent change to PDFTeX has caused magnification to apply to
page dimensions. This small package changes the values set in
the page dimension variables from pt to truept, thus evading
the effects of \mag.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/fixpdfmag/fixpdfmag.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
