Name:		texlive-fixpdfmag
Version:	20090917
Release:	1
Summary:	Fix magnification in PDFTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/misc/fixpdfmag.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixpdfmag.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A recent change to PDFTeX has caused magnification to apply to
page dimensions. This small package changes the values set in
the page dimension variables from pt to truept, thus evading
the effects of \mag.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/fixpdfmag/fixpdfmag.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
