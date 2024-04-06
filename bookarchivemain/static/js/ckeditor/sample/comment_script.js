ClassicEditor
	.create( document.querySelector( '#comment_text' ), {
		fontFamily: {
            options: [
              'Inter-VariableFont_slnt,wght.ttf'
            ]
        },
	} )
	.then( editor => {
		window.editor = editor;
	} )
	.catch( handleSampleError );

function handleSampleError( error ) {
	const issueUrl = 'https://github.com/ckeditor/ckeditor5/issues';

	const message = [
		'Oops, something went wrong!',
		`Please, report the following error on ${ issueUrl } with the build id "s09x29s5rl2m-fytv9e14y5w7" and the error stack trace:`
	].join( '\n' );

	console.error( message );
	console.error( error );
}
