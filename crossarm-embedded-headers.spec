#
# TODO:
#	-	Header files for Sharp ARM Based MCUs can be downloaded
#		from the BlueStreak software library web-site.
#		Currently at: http://able.sharpsma.com
#
Summary:	ARM header files (register definitions)
Name:		crossarm-embedded-headers
Version:	3.4
Release:	1
License:	GPL
Group:		Development
Source0:	http://www.ariusdsp.com/~gnuarm/gnuarm-%{version}-headers.zip
# Source0-md5:	9e4d7acf4d9be0eb8dd73572d0862036
URL:		http://www.gnuarm.org/
BuildRequires:	dos2unix
BuildRequires:	findutils
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		arm-pld-linux
%define		arch		%{_prefix}/%{target}

%description
This package contains register definitions files for ARM based MCUs.

%prep
%setup -q -c

%build
find -type f | xargs dos2unix

# kill bogus OKI readme
rm include/arch/oki/readme.txt

mv include/arch/atmel/readme.txt	readme-atmel.txt
mv include/arch/motorola/readme.txt	readme-motorola.txt
mv include/arch/philips/readme.txt	readme-philips.txt
mv include/arch/sharp/readme.txt	readme-sharp.txt
mv include/arch/st/readme.txt		readme-st.txt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{arch}
cp -r include $RPM_BUILD_ROOT%{arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme*
%dir %{arch}/include
%dir %{arch}/include/arch
%dir %{arch}/include/arch/atmel
%{arch}/include/arch/atmel/*.h
%dir %{arch}/include/arch/motorola
%{arch}/include/arch/motorola/*.h
%dir %{arch}/include/arch/oki
%{arch}/include/arch/oki/*.h
%dir %{arch}/include/arch/philips
%{arch}/include/arch/philips/*.h
#dir %{arch}/include/arch/sharp
#{arch}/include/arch/sharp/*.h
%dir %{arch}/include/arch/st
%dir %{arch}/include/arch/st/str71x
%{arch}/include/arch/st/str71x/*.h
