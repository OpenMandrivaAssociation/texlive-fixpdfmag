# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/misc/fixpdfmag.tex
# catalog-date 2009-09-17 21:16:39 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-fixpdfmag
Version:	20090917
Release:	6
Summary:	Fix magnification in PDFTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/misc/fixpdfmag.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixpdfmag.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090917-2
+ Revision: 751916
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090917-1
+ Revision: 718453
- texlive-fixpdfmag
- texlive-fixpdfmag
- texlive-fixpdfmag
- texlive-fixpdfmag

