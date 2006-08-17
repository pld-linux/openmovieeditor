diff -ur openmovieeditor-0.0.20060712-o/src/AudioFileFfmpeg.cxx openmovieeditor-0.0.20060712/src/AudioFileFfmpeg.cxx
--- openmovieeditor-0.0.20060712-o/src/AudioFileFfmpeg.cxx	2006-06-25 13:31:03.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/AudioFileFfmpeg.cxx	2006-08-17 01:58:04.000000000 -0600
@@ -65,9 +65,9 @@
 		ERROR_DETAIL( "avcodec_open failed" );
 		return;
 	}
-	if ( m_samplerate != 48000 ) {
+	if ( m_samplerate != 44100 ) {
 		CLEAR_ERRORS();
-		ERROR_DETAIL( "Audio samplerates other than 48000 are not supported" );
+		ERROR_DETAIL( "Audio samplerates other than 44100 are not supported" );
 		return;
 	}
 	if ( m_codecContext->channels != 2 && m_codecContext->channels != 1) {
diff -ur openmovieeditor-0.0.20060712-o/src/AudioFileQT.cxx openmovieeditor-0.0.20060712/src/AudioFileQT.cxx
--- openmovieeditor-0.0.20060712-o/src/AudioFileQT.cxx	2006-06-25 13:30:17.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/AudioFileQT.cxx	2006-08-17 02:02:04.000000000 -0600
@@ -52,9 +52,9 @@
 		return;
 	}
 	m_length = quicktime_audio_length( m_qt, 0 );
-	if ( quicktime_sample_rate( m_qt, 0 ) != 48000 ) {
+	if ( quicktime_sample_rate( m_qt, 0 ) != 44100 ) {
 		CLEAR_ERRORS();
-		ERROR_DETAIL( "Audio samplerates other than 48000 are not supported" );
+		ERROR_DETAIL( "Audio samplerates other than 44100 are not supported" );
 		return;
 	}
 	if ( quicktime_track_channels( m_qt, 0 ) != 2 ) {
diff -ur openmovieeditor-0.0.20060712-o/src/AudioFileQT.H openmovieeditor-0.0.20060712/src/AudioFileQT.H
--- openmovieeditor-0.0.20060712-o/src/AudioFileQT.H	2006-05-15 14:55:04.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/AudioFileQT.H	2006-08-17 01:59:36.000000000 -0600
@@ -39,7 +39,7 @@
 		void seek( int64_t sample );
 		int fillBuffer( float* output, unsigned long frames );
 			// sizof(output) == frames * 2
-			// File Format: 48000 stereo interleaved
+			// File Format: 44100 stereo interleaved
 	private:
 		quicktime_t* m_qt;
 		bool m_oneShot;
diff -ur openmovieeditor-0.0.20060712-o/src/AudioFileSnd.cxx openmovieeditor-0.0.20060712/src/AudioFileSnd.cxx
--- openmovieeditor-0.0.20060712-o/src/AudioFileSnd.cxx	2006-05-15 14:55:02.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/AudioFileSnd.cxx	2006-08-17 01:59:50.000000000 -0600
@@ -40,8 +40,8 @@
 		ERROR_DETAIL( "This is an empty audio file" );
 		return;
 	}
-	if ( sfinfo.samplerate != 48000 ) {
-		ERROR_DETAIL( "Audio samplerates other than 48000 are not supported" );
+	if ( sfinfo.samplerate != 44100 ) {
+		ERROR_DETAIL( "Audio samplerates other than 44100 are not supported" );
 		return;
 	}
 	m_length = sfinfo.frames;
diff -ur openmovieeditor-0.0.20060712-o/src/AudioTrack.H openmovieeditor-0.0.20060712/src/AudioTrack.H
--- openmovieeditor-0.0.20060712-o/src/AudioTrack.H	2006-06-14 02:58:36.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/AudioTrack.H	2006-08-17 02:03:02.000000000 -0600
@@ -40,7 +40,7 @@
 		void addFile( int64_t position, string filename, int64_t trimA = 0, int64_t trimB = 0, int mute = 0, int id = -1, int64_t length = -1 );
 		int type() { return TRACK_TYPE_AUDIO; }
 		void sort();
-		float stretchFactor() { return ( 48000 / g_fps ); }
+		float stretchFactor() { return ( 44100 / g_fps ); }
 		int64_t soundLength();
 };
 	
diff -ur openmovieeditor-0.0.20060712-o/src/Codecs.cxx openmovieeditor-0.0.20060712/src/Codecs.cxx
--- openmovieeditor-0.0.20060712-o/src/Codecs.cxx	2006-06-25 12:21:27.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/Codecs.cxx	2006-08-17 01:59:12.000000000 -0600
@@ -312,8 +312,8 @@
 }
 void CodecParameters::set( quicktime_t* qt, int w, int h )
 {
-	lqt_add_audio_track( qt, 2, 48000, 16, m_currentAudioCodec->codecInfo );
-	lqt_add_video_track( qt, w, h, 1200, 30000, m_currentVideoCodec->codecInfo ); // 30000 / 1200 == 25
+	lqt_add_audio_track( qt, 2, 44100, 16, m_currentAudioCodec->codecInfo );
+	lqt_add_video_track( qt, w, h, 1001, 30000, m_currentVideoCodec->codecInfo ); // 30000 / 1200 == 25
 
 	param_node* p;
 	for ( p = m_currentAudioCodec->parameters; p; p = p->next ) {
diff -ur openmovieeditor-0.0.20060712-o/src/IAudioFile.H openmovieeditor-0.0.20060712/src/IAudioFile.H
--- openmovieeditor-0.0.20060712-o/src/IAudioFile.H	2006-05-15 14:55:00.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/IAudioFile.H	2006-08-17 01:57:49.000000000 -0600
@@ -36,7 +36,7 @@
 		virtual void seek( int64_t sample ) = 0;
 		virtual int fillBuffer( float* output, unsigned long frames ) = 0;
 			//sizof(output) = frames * 2
-			//File Format: 48000 stereo interleaved
+			//File Format: 44100 stereo interleaved
 		inline string filename() { return m_filename; }
 	protected:
 		int64_t m_length;
diff -ur openmovieeditor-0.0.20060712-o/src/nle.cxx openmovieeditor-0.0.20060712/src/nle.cxx
--- openmovieeditor-0.0.20060712-o/src/nle.cxx	2006-07-10 16:06:42.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/nle.cxx	2006-08-17 02:01:24.000000000 -0600
@@ -36,7 +36,7 @@
 if ( dlg.go && strcmp( "", dlg.export_filename->value() ) != 0 ) {
 	ProgressDialog pDlg( "Rendering Project" );
 	render_frame_size* fs = (render_frame_size*)dlg.frameSize();
-	nle::Renderer ren( dlg.export_filename->value(), fs->x, fs->y, 25, 48000, &cp );
+	nle::Renderer ren( dlg.export_filename->value(), fs->x, fs->y, 29, 44100, &cp );
 
 	/* stop playback before starting to render... */
 	g_playButton->label( "@>" );
@@ -772,17 +772,17 @@
 }
 
 Fl_Menu_Item EncodeDialog::menu_Samplerate[] = {
- {"48000", 0,  0, 0, 0, 0, 0, 14, 56},
+ {"44100", 0,  0, 0, 0, 0, 0, 14, 56},
  {0,0,0,0,0,0,0,0,0}
 };
 
 Fl_Menu_Item EncodeDialog::menu_Framerate[] = {
- {"25 (PAL)", 0,  0, 0, 0, 0, 0, 14, 56},
+ {"29.97 (NTSC)", 0,  0, 0, 0, 0, 0, 14, 56},
  {0,0,0,0,0,0,0,0,0}
 };
 
 Fl_Menu_Item EncodeDialog::menu_frame_size_choice[] = {
- {"720x576", 0,  0, (void*)(&fs720x576), 0, 0, 0, 14, 56},
+ {"720x480", 0,  0, (void*)(&fs720x480), 0, 0, 0, 14, 56},
  {"360x288", 0,  0, (void*)(&fs360x288), 0, 0, 0, 14, 56},
  {"640x480", 0,  0, (void*)(&fs640x480), 0, 0, 0, 14, 56},
  {"320x240", 0,  0, (void*)(&fs320x240), 0, 0, 0, 14, 56},
diff -ur openmovieeditor-0.0.20060712-o/src/nle.fl openmovieeditor-0.0.20060712/src/nle.fl
--- openmovieeditor-0.0.20060712-o/src/nle.fl	2006-07-10 16:06:41.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/nle.fl	2006-08-17 02:04:10.000000000 -0600
@@ -42,7 +42,7 @@
 if ( dlg.go && strcmp( "", dlg.export_filename->value() ) != 0 ) {
 	ProgressDialog pDlg( "Rendering Project" );
 	render_frame_size* fs = (render_frame_size*)dlg.frameSize();
-	nle::Renderer ren( dlg.export_filename->value(), fs->x, fs->y, 25, 48000, &cp );
+	nle::Renderer ren( dlg.export_filename->value(), fs->x, fs->y, 29, 44100, &cp );
 
 	/* stop playback before starting to render... */
 	g_playButton->label( "@>" );
@@ -447,7 +447,7 @@
         xywh {145 250 205 25} down_box BORDER_BOX
       } {
         menuitem {} {
-          label 48000
+          label 44100
           xywh {0 0 100 20}
         }
       }
@@ -456,7 +456,7 @@
         xywh {145 130 205 25} down_box BORDER_BOX
       } {
         menuitem {} {
-          label {25 (PAL)}
+          label {29.97 (NTSC)}
           xywh {0 0 100 20}
         }
       }
@@ -465,8 +465,8 @@
         xywh {145 160 205 25} down_box BORDER_BOX
       } {
         menuitem {} {
-          label 720x576
-          user_data {&fs720x576}
+          label 720x480
+          user_data {&fs720x480}
           xywh {0 0 100 20}
         }
         menuitem {} {
diff -ur openmovieeditor-0.0.20060712-o/src/Renderer.cxx openmovieeditor-0.0.20060712/src/Renderer.cxx
--- openmovieeditor-0.0.20060712-o/src/Renderer.cxx	2006-06-23 11:54:29.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/Renderer.cxx	2006-08-17 02:05:23.000000000 -0600
@@ -31,7 +31,7 @@
 #include "Codecs.H"
 #include "render_helper.H"
 
-render_frame_size fs720x576 = { 720, 576 };
+render_frame_size fs720x480 = { 720, 480 };
 render_frame_size fs360x288 = { 360, 288 };
 render_frame_size fs640x480 = { 640, 480 };
 render_frame_size fs320x240 = { 320, 240 };
@@ -70,7 +70,7 @@
 	}
 #endif
 	lqt_codec_info_t *codec = codecs[7];
-	lqt_add_audio_track( qt, 2, 48000, 16, codec );
+	lqt_add_audio_track( qt, 2, 44100, 16, codec );
 	lqt_destroy_codec_info( codecs );
 	codecs = lqt_query_registry( 0, 1, 1, 0 );
 #if 0
@@ -169,10 +169,10 @@
 	}
 	
 	do {
-		if ( fcnt >= 1920 ) { // 1601 für NTSC, 1920 für PAL
+		if ( fcnt >= 1471 ) { // 1601 für NTSC, 1920 für PAL
 			g_timeline->getBlendedFrame( &enc_frame );
 			quicktime_encode_video( qt, enc_frame.rows, 0 );
-			fcnt -= 1920;
+			fcnt -= 1471;
 			current_frame++;
 			if ( l ) {
 				if ( l->progress( current_frame * 100 / length ) ) {
diff -ur openmovieeditor-0.0.20060712-o/src/Renderer.H openmovieeditor-0.0.20060712/src/Renderer.H
--- openmovieeditor-0.0.20060712-o/src/Renderer.H	2006-05-15 14:55:01.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/Renderer.H	2006-08-17 02:04:25.000000000 -0600
@@ -29,7 +29,7 @@
 	int y;
 } render_frame_size;
 
-extern render_frame_size fs720x576;
+extern render_frame_size fs720x480;
 extern render_frame_size fs360x288;
 extern render_frame_size fs640x480;
 extern render_frame_size fs320x240;
diff -ur openmovieeditor-0.0.20060712-o/src/SimplePlaybackCore.cxx openmovieeditor-0.0.20060712/src/SimplePlaybackCore.cxx
--- openmovieeditor-0.0.20060712-o/src/SimplePlaybackCore.cxx	2006-06-21 14:28:34.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/SimplePlaybackCore.cxx	2006-08-17 02:05:31.000000000 -0600
@@ -230,13 +230,13 @@
 	/* Calculate frame. */
 	jack_transport_query(jack_client, &jack_position);
 	jack_time = jack_position.frame / (double) jack_position.frame_rate;
-	frame = (int) rint(25.0 * jack_time );
+	frame = (int) rint(29.97 * jack_time );
 	return(frame);
 }
 
 void jack_reposition(int vframe)
 {
-	jack_nframes_t frame= 48000/25 * vframe;
+	jack_nframes_t frame= (int)(44100/29.97 * vframe);
 	if (jack_client)
 		jack_transport_locate (jack_client, frame);
 }
@@ -273,7 +273,7 @@
 }
 void SimplePlaybackCore::play()
 {
-	int scrublen = 3*1920;  // TODO: get from preferences :  scrub_freq = sample_rate/scrublen   
+	int scrublen = 3*1471;  // TODO: get from preferences :  scrub_freq = sample_rate/scrublen   
 				// good values for scrub_freq are 1..50 Hz
 				// scrub length is rounded up to next multiple of jack buffer size.
 	if ( m_active ) {
@@ -288,7 +288,7 @@
 		m_scrubmax = (jack_bufsiz!=0)?(int)ceil(scrublen/jack_bufsiz):1;
 
 		if (!g_use_jack_transport) {
-			m_audioPosition = m_currentFrame * ( 48000 / 25 ); 
+			m_audioPosition = m_currentFrame * (int)( 44100 / 29.97 ); 
 		} else {
 			jack_reposition(m_currentFrame);
 
@@ -306,13 +306,13 @@
 	} else { // portaudio
 		m_currentFrame = g_timeline->m_seekPosition;
 		m_lastFrame = g_timeline->m_seekPosition;
-		m_audioPosition = m_currentFrame * ( 48000 / 25 );
+		m_audioPosition = m_currentFrame * (int)( 44100 / 29.97 );
 		m_audioReader->sampleseek(1, m_audioPosition); // set absolute audio sample start position
 	}
 
 	if (g_use_jack_transport) jack_play();
 
-	if (jack_connected() || portaudio_start( 48000, FRAMES, this ) ) 
+	if (jack_connected() || portaudio_start( 44100, FRAMES, this ) ) 
 	{
 		m_active = true;
 		Fl::add_timeout( 0.1, timer_callback, this );
@@ -407,9 +407,9 @@
 	m_audioReader->sampleseek(0,r); // set relative sample position;
 	m_audioPosition += r;
 	pthread_mutex_lock( &condition_mutex );
-	m_currentFrame = m_audioPosition / ( 48000 / 25 ); //FIXME: highly dependent from 'frames' :(
+	m_currentFrame = m_audioPosition / (int)( 44100 / 29.97 ); //FIXME: highly dependent from 'frames' :(
 	pthread_cond_signal( &condition_cond );
-	/*if ( m_audioPosition / ( 48000 / 25 ) > m_currentFrame ) {
+	/*if ( m_audioPosition / (int)( 44100 / 29.97 ) > m_currentFrame ) {
 		//cout << "m_audioPosition: " << m_audioPosition << " m_currentFrame: " << m_currentFrame << " frames: " << frames << endl;
 		m_currentFrame++;
 		pthread_cond_signal( &condition_cond );
@@ -448,7 +448,7 @@
 	} else if (jack_connected()) { // jack audio with local transport
 		// FIXME: for larger jack buffer sizes, this can become inaccurate due to rounding
 		// issues. -> do something similar as the portaudio drift sync...
-		m_lastFrame = (int64_t)rintl(m_audioPosition*25/48000);
+		m_lastFrame = (int64_t)rintl(m_audioPosition*(int)(29.97/44100));
 	} else { // portaudio
 		m_lastFrame++;
 		pthread_mutex_lock( &condition_mutex );
diff -ur openmovieeditor-0.0.20060712-o/src/Timeline.cxx openmovieeditor-0.0.20060712/src/Timeline.cxx
--- openmovieeditor-0.0.20060712-o/src/Timeline.cxx	2006-06-27 06:31:05.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/Timeline.cxx	2006-08-17 02:03:16.000000000 -0600
@@ -94,13 +94,13 @@
 {
 	TimelineBase::sort();
 	m_playPosition = m_seekPosition;
-	m_samplePosition = int64_t( m_seekPosition * ( 48000 / g_fps ) );
+	m_samplePosition = int64_t( m_seekPosition * ( 44100 / g_fps ) );
 	{
 		int64_t audio_max = 0;
 		int64_t video_max = 0;
 		sl_map( m_allTracks, audio_length_helper, &audio_max );
 		sl_map( m_allTracks, video_length_helper, &video_max );
-		video_max = (int64_t)( video_max * ( 48000 / g_fps ) );
+		video_max = (int64_t)( video_max * ( 44100 / g_fps ) );
 		m_soundLength = video_max > audio_max ? video_max : audio_max;
 	}
 }
diff -ur openmovieeditor-0.0.20060712-o/src/Timeline.H openmovieeditor-0.0.20060712/src/Timeline.H
--- openmovieeditor-0.0.20060712-o/src/Timeline.H	2006-06-27 06:28:20.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/Timeline.H	2006-08-17 02:00:35.000000000 -0600
@@ -50,7 +50,7 @@
 		inline void sampleseek( int mode, int64_t position )
 		{
 			if (mode) m_samplePosition = position; else m_samplePosition += position;
-			/* m_playPosition = m_samplePosition*25/48000; m_seekPosition= m_playPosition;*/
+			/* m_playPosition = m_samplePosition*25/44100; m_seekPosition= m_playPosition;*/
 		}
 		inline int64_t soundLength() { return m_soundLength; }
 		bool changed() { return m_changed; }
diff -ur openmovieeditor-0.0.20060712-o/src/VideoClip.cxx openmovieeditor-0.0.20060712/src/VideoClip.cxx
--- openmovieeditor-0.0.20060712-o/src/VideoClip.cxx	2006-05-15 14:55:05.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/VideoClip.cxx	2006-08-17 01:59:31.000000000 -0600
@@ -60,7 +60,7 @@
 }
 int64_t VideoClip::maxAudioLength()
 {
-	return m_videoFile->length() * (int64_t)( 48000 / g_fps );
+	return m_videoFile->length() * (int64_t)( 44100 / g_fps );
 }
 int64_t VideoClip::length()
 {
@@ -68,17 +68,17 @@
 }
 int64_t VideoClip::audioTrimA()
 {
-	return m_trimA * (int64_t)( 48000 / g_fps );
+	return m_trimA * (int64_t)( 44100 / g_fps );
 }
 int64_t VideoClip::audioTrimB()
 {
-	int64_t r = m_trimB * (int64_t)( 48000 / g_fps );
+	int64_t r = m_trimB * (int64_t)( 44100 / g_fps );
 	int64_t t = m_audioFile->length() - maxAudioLength() + r;
 	return t < 0 ? 0 : t;
 }
 int64_t VideoClip::audioPosition()
 {
-	return m_position * (int64_t)( 48000 / g_fps );
+	return m_position * (int64_t)( 44100 / g_fps );
 }
 void VideoClip::reset()
 {
diff -ur openmovieeditor-0.0.20060712-o/src/VideoFileFfmpeg.cxx openmovieeditor-0.0.20060712/src/VideoFileFfmpeg.cxx
--- openmovieeditor-0.0.20060712-o/src/VideoFileFfmpeg.cxx	2006-06-25 06:35:56.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/VideoFileFfmpeg.cxx	2006-08-17 01:55:54.000000000 -0600
@@ -97,10 +97,10 @@
 	//m_formatContext->streams[m_videoStream]->r_frame_rate;
 	//time_base
 	m_framerate = av_q2d( m_formatContext->streams[m_videoStream]->r_frame_rate );
-	if ( m_framerate < 24.9 || m_framerate > 25.1 ) {
+	if ( m_framerate < 29 || m_framerate > 30.1 ) {
 		CLEAR_ERRORS();
 		cout << "Wrong Framerate: " << m_framerate << endl;
-		ERROR_DETAIL( "Video framerates other than 25 are not supported" );
+		ERROR_DETAIL( "Video framerates other than 29.97 are not supported" );
 		return;
 	}
 
diff -ur openmovieeditor-0.0.20060712-o/src/VideoTrack.cxx openmovieeditor-0.0.20060712/src/VideoTrack.cxx
--- openmovieeditor-0.0.20060712-o/src/VideoTrack.cxx	2006-06-25 13:43:55.000000000 -0600
+++ openmovieeditor-0.0.20060712/src/VideoTrack.cxx	2006-08-17 02:05:37.000000000 -0600
@@ -236,10 +236,10 @@
 	while ( m_current && m_current->clip->type() != CLIP_TYPE_VIDEO && m_current->clip->type() != CLIP_TYPE_AUDIO ) {
 		m_current = m_current->next;
 	}
-	while ( m_currentAudioFadeOver && fade_over_end( m_currentAudioFadeOver ) * 1920 < position + frames  ) { // 48000 / 25 == 1920
+	while ( m_currentAudioFadeOver && fade_over_end( m_currentAudioFadeOver ) * 1471 < position + frames  ) { // 44100 / 29.97 == 1471
 		m_currentAudioFadeOver = m_currentAudioFadeOver->next;
 	}
-	if ( m_currentAudioFadeOver && position > fade_over_start( m_currentAudioFadeOver ) * 1920 ) {
+	if ( m_currentAudioFadeOver && position > fade_over_start( m_currentAudioFadeOver ) * 1471 ) {
 		AudioClipBase* ac1 = dynamic_cast<AudioClipBase*>(m_currentAudioFadeOver->clipA);
 		AudioClipBase* ac2 = dynamic_cast<AudioClipBase*>(m_currentAudioFadeOver->clipB);
 		for ( int i = (frames * 2) - 1; i >= 0; i-- ) {
