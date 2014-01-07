# Include this gypi to include all public header files that exist in the
# include directory.
#
# The list is computed by running 'find include -name *.h' in the root dir of
# the project.
#
{
  'variables': {
    'header_filenames': [
      'pdf/SkPDFDevice.h',
      'pdf/SkPDFDocument.h',
      'svg/SkSVGTypes.h',
      'svg/SkSVGBase.h',
      'svg/SkSVGAttribute.h',
      'svg/SkSVGParser.h',
      'svg/SkSVGPaintState.h',
      'animator/SkAnimator.h',
      'animator/SkAnimatorView.h',
      'gpu/GrTexture.h',
      'gpu/SkGr.h',
      'gpu/GrContext.h',
      'gpu/gl/GrGLConfig_chrome.h',
      'gpu/gl/SkNativeGLContext.h',
      'gpu/gl/SkMesaGLContext.h',
      'gpu/gl/SkDebugGLContext.h',
      'gpu/gl/SkANGLEGLContext.h',
      'gpu/gl/GrGLConfig.h',
      'gpu/gl/GrGLInterface.h',
      'gpu/gl/SkNullGLContext.h',
      'gpu/gl/GrGLFunctions.h',
      'gpu/gl/SkGLContextHelper.h',
      'gpu/gl/GrGLExtensions.h',
      'gpu/SkGpuDevice.h',
      'gpu/GrTypes.h',
      'gpu/GrFontScaler.h',
      'gpu/GrResource.h',
      'gpu/GrKey.h',
      'gpu/GrOvalRenderer.h',
      'gpu/GrEffectUnitTest.h',
      'gpu/GrConfig.h',
      'gpu/GrPaint.h',
      'gpu/GrPathRendererChain.h',
      'gpu/GrTBackendEffectFactory.h',
      'gpu/GrDrawEffect.h',
      'gpu/GrTextContext.h',
      'gpu/GrEffect.h',
      'gpu/SkGrTexturePixelRef.h',
      'gpu/GrTextureAccess.h',
      'gpu/GrRect.h',
      'gpu/GrEffectStage.h',
      'gpu/GrClipData.h',
      'gpu/GrUserConfig.h',
      'gpu/SkGrPixelRef.h',
      'gpu/GrAARectRenderer.h',
      'gpu/GrColor.h',
      'gpu/GrGlyph.h',
      'gpu/GrBackendEffectFactory.h',
      'gpu/GrContextFactory.h',
      'gpu/GrRenderTarget.h',
      'gpu/GrSurface.h',
      'gpu/GrTypesPriv.h',
      'gpu/GrPoint.h',
      'config/sk_stdint.h',
      'config/SkUserConfig.h',
      'pipe/SkGPipe.h',
      'images/SkImageRef.h',
      'images/SkMovie.h',
      'images/SkPageFlipper.h',
      'images/SkForceLinking.h',
      'images/SkImageRef_GlobalPool.h',
      'images/SkImages.h',
      'effects/SkMorphologyImageFilter.h',
      'effects/Sk2DPathEffect.h',
      'effects/SkXfermodeImageFilter.h',
      'effects/SkArithmeticMode.h',
      'effects/SkMergeImageFilter.h',
      'effects/SkPerlinNoiseShader.h',
      'effects/SkLerpXfermode.h',
      'effects/SkLumaColorFilter.h',
      'effects/SkRectShaderImageFilter.h',
      'effects/SkMagnifierImageFilter.h',
      'effects/SkBicubicImageFilter.h',
      'effects/SkPorterDuff.h',
      'effects/SkBlurImageFilter.h',
      'effects/SkKernel33MaskFilter.h',
      'effects/SkTableMaskFilter.h',
      'effects/SkAvoidXfermode.h',
      'effects/SkBitmapSource.h',
      'effects/SkCornerPathEffect.h',
      'effects/SkTransparentShader.h',
      'effects/SkStippleMaskFilter.h',
      'effects/SkPaintFlagsDrawFilter.h',
      'effects/SkOffsetImageFilter.h',
      'effects/SkDiscretePathEffect.h',
      'effects/SkTableColorFilter.h',
      'effects/SkGradientShader.h',
      'effects/SkEmbossMaskFilter.h',
      'effects/SkComposeImageFilter.h',
      'effects/SkTestImageFilters.h',
      'effects/SkLayerRasterizer.h',
      'effects/SkDashPathEffect.h',
      'effects/Sk1DPathEffect.h',
      'effects/SkBlurMaskFilter.h',
      'effects/SkDrawExtraPathEffect.h',
      'effects/SkDisplacementMapEffect.h',
      'effects/SkPixelXorXfermode.h',
      'effects/SkColorMatrixFilter.h',
      'effects/SkColorMatrix.h',
      'effects/SkBlurDrawLooper.h',
      'effects/SkColorFilterImageFilter.h',
      'effects/SkLayerDrawLooper.h',
      'effects/SkLightingImageFilter.h',
      'effects/SkDropShadowImageFilter.h',
      'effects/SkMatrixConvolutionImageFilter.h',
      'utils/win/SkAutoCoInitialize.h',
      'utils/win/SkHRESULT.h',
      'utils/win/SkIStream.h',
      'utils/win/SkTScopedComPtr.h',
      'utils/SkBoundaryPatch.h',
      'utils/SkUnitMappers.h',
      'utils/SkPictureUtils.h',
      'utils/SkRandom.h',
      'utils/SkMeshUtils.h',
      'utils/SkCullPoints.h',
      'utils/SkCamera.h',
      'utils/SkLua.h',
      'utils/SkParsePaint.h',
      'utils/SkCountdown.h',
      'utils/SkRunnable.h',
      'utils/SkParse.h',
      'utils/SkThreadPool.h',
      'utils/SkMatrix44.h',
      'utils/SkInterpolator.h',
      'utils/SkWGL.h',
      'utils/SkDumpCanvas.h',
      'utils/SkRTConf.h',
      'utils/SkCubicInterval.h',
      'utils/SkLuaCanvas.h',
      'utils/SkDebugUtils.h',
      'utils/SkLayer.h',
      'utils/SkProxyCanvas.h',
      'utils/SkNWayCanvas.h',
      'utils/SkPathUtils.h',
      'utils/SkDeferredCanvas.h',
      'utils/ios/SkStream_NSData.h',
      'utils/SkNullCanvas.h',
      'utils/SkParsePath.h',
      'utils/SkJSON.h',
      'utils/SkCondVar.h',
      'utils/SkNinePatch.h',
      'utils/mac/SkCGUtils.h',
      'xml/SkDOM.h',
      'xml/SkJS.h',
      'xml/SkXMLParser.h',
      'xml/SkBML_XMLParser.h',
      'xml/SkBML_WXMLParser.h',
      'xml/SkXMLWriter.h',
      'device/xps/SkXPSDevice.h',
      'device/xps/SkConstexprMath.h',
      'ports/SkTypeface_win.h',
      'ports/SkHarfBuzzFont.h',
      'ports/SkFontConfigInterface.h',
      'ports/SkTypeface_mac.h',
      'ports/SkTypeface_android.h',
      'ports/SkFontStyle.h',
      'ports/SkFontMgr.h',
      'text/SkTextLayout.h',
      'core/SkColor.h',
      'core/SkFontHost.h',
      'core/SkMetaData.h',
      'core/SkRRect.h',
      'core/SkMatrix.h',
      'core/SkDataTable.h',
      'core/SkScalar.h',
      'core/SkFlattenableSerialization.h',
      'core/SkTypeface.h',
      'core/SkImageEncoder.h',
      'core/SkDrawFilter.h',
      'core/SkTDict.h',
      'core/SkRasterizer.h',
      'core/SkColorPriv.h',
      'core/SkFloatingPoint.h',
      'core/SkOSFile.h',
      'core/SkPaint.h',
      'core/SkTDStack.h',
      'core/SkDither.h',
      'core/SkFixed.h',
      'core/SkDocument.h',
      'core/SkInstCnt.h',
      'core/SkEndian.h',
      'core/SkColorTable.h',
      'core/SkBitmap.h',
      'core/SkDraw.h',
      'core/SkPackBits.h',
      'core/SkFloatBits.h',
      'core/SkDeque.h',
      'core/SkTRegistry.h',
      'core/Sk64.h',
      'core/SkTLazy.h',
      'core/SkComposeShader.h',
      'core/SkUtils.h',
      'core/SkImage.h',
      'core/SkTileGridPicture.h',
      'core/SkPaintOptionsAndroid.h',
      'core/SkDeviceProperties.h',
      'core/SkGraphics.h',
      'core/SkCanvas.h',
      'core/SkPicture.h',
      'core/SkClipStack.h',
      'core/SkXfermode.h',
      'core/SkColorFilter.h',
      'core/SkRegion.h',
      'core/SkRefCnt.h',
      'core/SkStream.h',
      'core/SkFontLCDConfig.h',
      'core/SkBlitRow.h',
      'core/SkGeometry.h',
      'core/SkStrokeRec.h',
      'core/SkImageDecoder.h',
      'core/SkTime.h',
      'core/SkPathMeasure.h',
      'core/SkMaskFilter.h',
      'core/SkBounder.h',
      'core/SkFlate.h',
      'core/SkTDArray.h',
      'core/SkAnnotation.h',
      'core/SkChecksum.h',
      'core/SkMath.h',
      'core/SkDrawLooper.h',
      'core/SkThread_platform.h',
      'core/SkFlattenableBuffers.h',
      'core/SkTemplates.h',
      'core/SkMask.h',
      'core/SkMallocPixelRef.h',
      'core/SkWeakRefCnt.h',
      'core/SkTypes.h',
      'core/SkThread.h',
      'core/SkData.h',
      'core/SkPoint.h',
      'core/SkColorShader.h',
      'core/SkChunkAlloc.h',
      'core/SkUnPreMultiply.h',
      'core/SkReader32.h',
      'core/SkDevice.h',
      'core/SkImageFilter.h',
      'core/SkAdvancedTypefaceMetrics.h',
      'core/SkTInternalLList.h',
      'core/SkTArray.h',
      'core/SkStringUtils.h',
      'core/SkPreConfig.h',
      'core/SkImageFilterUtils.h',
      'core/SkLineClipper.h',
      'core/SkPathEffect.h',
      'core/SkString.h',
      'core/SkPixelRef.h',
      'core/SkSize.h',
      'core/SkEmptyShader.h',
      'core/SkSurface.h',
      'core/SkPostConfig.h',
      'core/SkShader.h',
      'core/SkWriter32.h',
      'core/SkError.h',
      'core/SkPath.h',
      'core/SkTrace.h',
      'core/SkUnitMapper.h',
      'core/SkFlattenable.h',
      'core/SkTSearch.h',
      'core/SkRect.h',
      'pathops/SkPathOps.h',
      'views/SkTouchGesture.h',
      'views/SkEvent.h',
      'views/SkOSWindow_NaCl.h',
      'views/SkTextBox.h',
      'views/SkViewInflate.h',
      'views/SkOSWindow_iOS.h',
      'views/SkBGViewArtist.h',
      'views/SkOSWindow_SDL.h',
      'views/SkWindow.h',
      'views/SkSystemEventTypes.h',
      'views/SkOSWindow_Android.h',
      'views/SkOSWindow_Mac.h',
      'views/android/AndroidKeyToSkKey.h',
      'views/SkEventSink.h',
      'views/animated/SkImageView.h',
      'views/animated/SkWidgetViews.h',
      'views/animated/SkProgressBarView.h',
      'views/animated/SkBorderView.h',
      'views/animated/SkScrollBarView.h',
      'views/SkStackViewLayout.h',
      'views/SkApplication.h',
      'views/unix/keysym2ucs.h',
      'views/unix/XkeysToSkKeys.h',
      'views/SkKey.h',
      'views/SkView.h',
      'views/SkOSMenu.h',
      'views/SkOSWindow_Unix.h',
      'views/SkWidget.h',
      'views/SkOSWindow_Win.h',
    ],
  },
}
